# python tools/PostgreSQL/scripts/create_postgres_db.py




import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connection details for the PostgreSQL server (not the database yet)
server = os.getenv('DB_SERVER')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT', 5432)  # Default PostgreSQL port
database = os.getenv('DB_DATABASE')

def create_database(server, username, password, port, database):
    """
    Creates a PostgreSQL database if it doesn't already exist.

    :param server: PostgreSQL server address
    :param username: Username for authentication
    :param password: Password for authentication
    :param port: Port number for PostgreSQL
    :param database: Name of the database to create
    """
    try:
        # Connect to the PostgreSQL server (default database is 'postgres')
        connection = psycopg2.connect(
            host=server,
            user=username,
            password=password,
            port=port,
            database="postgres"  # Connect to the default 'postgres' database
        )
        connection.autocommit = True  # Enable autocommit for database creation
        cursor = connection.cursor()

        # Check if the database already exists
        cursor.execute(
            sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"),
            [database]
        )
        exists = cursor.fetchone()

        if not exists:
            # Create the database if it doesn't exist
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database)))
            print(f"Database '{database}' created successfully.")
        else:
            print(f"Database '{database}' already exists.")

    except psycopg2.Error as e:
        print("Error while creating the database:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Call the function to create the database
create_database(server, username, password, port, database)