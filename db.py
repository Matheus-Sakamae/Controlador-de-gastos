import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_connection():
    config = {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
    }
    return mysql.connector.connect(**config)

con = get_connection()
con.close()
print("✅ OK")