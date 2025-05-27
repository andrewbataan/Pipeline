import pandas as pd
import psycopg2
import re
import os
from datetime import datetime

# VE 
DB_USER = os.environ.get("DB_CREDENTIALS_USR")
DB_PASSWORD = os.environ.get("DB_CREDENTIALS_PSW")

if not DB_USER or not DB_PASSWORD:
    raise ValueError("Credentials dosent match with Jenkins")

# Conection to postgres
try:
    conn = psycopg2.connect(
        dbname="product_db",
        user=DB_USER,
        password=DB_PASSWORD,
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
except Exception as e:
    print(f"Error de conexión: {e}")
    raise

# create table if not exist
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        email TEXT
    )
    """)
    conn.commit()
except Exception as e:
    print(f"Error to create table: {e}")
    conn.rollback()
    raise

# read and clean data
try:
    df = pd.read_csv("data/products.csv")
    cleaned = df.dropna(subset=["name", "price", "email"])
    cleaned = cleaned[cleaned["email"].apply(lambda x: re.match(r"[^@]+@[^@]+\.[^@]+", str(x)) is not None)]
except Exception as e:
    print(f"Error to process CSV: {e}")
    raise

# insert into table of Postgres
try:
    cursor.execute("DELETE FROM products")
    for _, row in cleaned.iterrows():
        cursor.execute(
            "INSERT INTO products (id, name, price, email) VALUES (%s, %s, %s, %s)",
            (int(row["id"]), row["name"], float(row["price"]), row["email"])
        )
    conn.commit()
except Exception as e:
    print(f"Error to insert data table: {e}")
    conn.rollback()
    raise
finally:
    cursor.close()
    conn.close()

# create logs
try:
    os.makedirs("logs", exist_ok=True)
    with open("logs/pipeline.log", "a") as log:
        log.write(f"{datetime.now()} - Loaded {len(cleaned)} row in PostgreSQL\n")
except Exception as e:
    print(f"Error to generate logs: {e}")
    raise