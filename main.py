import pandas as pd
import psycopg2
import re
import os
from datetime import datetime

# Conexión a PostgreSQL usando variables de entorno de Jenkins
try:
    conn = psycopg2.connect(
        dbname="product_db",
        user=os.environ.get("DB_CREDENTIALS_USR"),  # Usuario desde Jenkins
        password=os.environ.get("DB_CREDENTIALS_PSW"),  # Contraseña desde Jenkins
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
except Exception as e:
    print(f"Error de conexión: {e}")
    raise  # Fuerza el fallo del pipeline si hay error

# Crear tabla si no existe
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
    print(f"Error al crear tabla: {e}")
    conn.rollback()

# Leer y limpiar datos
try:
    df = pd.read_csv("data/products.csv")
    cleaned = df.dropna(subset=["name", "price", "email"])
    cleaned = cleaned[cleaned["email"].apply(lambda x: re.match(r"[^@]+@[^@]+\.[^@]+", str(x)) is not None)]
except Exception as e:
    print(f"Error al procesar CSV: {e}")
    raise

# Insertar datos en PostgreSQL
try:
    cursor.execute("DELETE FROM products")
    for _, row in cleaned.iterrows():
        cursor.execute(
            "INSERT INTO products (id, name, price, email) VALUES (%s, %s, %s, %s)",
            (int(row["id"]), row["name"], float(row["price"]), row["email"])
        )
    conn.commit()
except Exception as e:
    print(f"Error al insertar datos: {e}")
    conn.rollback()
    raise
finally:
    cursor.close()
    conn.close()

# Generar logs
try:
    with open("logs/pipeline.log", "a") as log:
        log.write(f"{datetime.now()} - Cargadas {len(cleaned)} filas en PostgreSQL\n")
except Exception as e:
    print(f"Error al generar logs: {e}")
    raise