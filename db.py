import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

con = mysql.connector.connect(**config)
con.close()
print("✅ OK")