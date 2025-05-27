import pandas as pd
import psycopg2
import re
from datetime import datetime

# Conexion to postgres
conn = psycopg2.connect(
    dbname="product_db",
    user="postgres",
    password="admin",        
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create table if not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    email TEXT
)
""")
conn.commit()

# Read CSV
df = pd.read_csv("data/products.csv")

# Validate email using regex
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", str(email))

# Clean data
cleaned = df.dropna(subset=["name", "price", "email"])
cleaned = cleaned[cleaned["email"].apply(is_valid_email)]

# empty the table
cursor.execute("DELETE FROM products")
conn.commit()

# Insert into databases
for _, row in cleaned.iterrows():
    cursor.execute(
        "INSERT INTO products (id, name, price, email) VALUES (%s, %s, %s, %s)",
        (int(row["id"]), row["name"], float(row["price"]), row["email"])
    )

conn.commit()

# Logs
with open("logs/pipeline.log", "a") as log:
    log.write(f"{datetime.now()} - Loaded {len(cleaned)} row to PostgreSQL\n")

cursor.close()
conn.close()