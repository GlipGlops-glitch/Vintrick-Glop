# ---- list_tables.py
# ---- python tools/PostgreSQL/scripts/list_tables.py
# ---- This script connects to a PostgreSQL database and lists all tables in the public schema.


import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection details from .env
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT', 5432)  # Default PostgreSQL port

def list_tables(server, database, username, password, port):
    """
    Connects to the PostgreSQL database and lists all tables in the public schema.
    """
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=server,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()

        # Query to list all tables in the public schema
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public';
        """)

        tables = cursor.fetchall()
        print("Tables in the public schema:")
        for table in tables:
            print(f"- {table[0]}")

    except psycopg2.Error as e:
        print("Error while connecting to the database:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Call the function to list tables
list_tables(server, database, username, password, port)