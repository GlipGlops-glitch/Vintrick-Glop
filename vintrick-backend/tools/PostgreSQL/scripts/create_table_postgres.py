# --- create_table_postgres.py
# --- python tools/PostgreSQL/scripts/create_table_postgres.py
# --- This script executes a SQL query to create a table in a PostgreSQL database.


import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

def execute_sql_query(server, database, username, password, port, query):
    """
    Executes a given SQL query on the specified PostgreSQL database.

    :param server: PostgreSQL server address
    :param database: Database name
    :param username: Username for authentication
    :param password: Password for authentication
    :param port: Port number for PostgreSQL
    :param query: SQL query to execute
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
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully.")
    except psycopg2.Error as e:
        print("Error while executing SQL query:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()