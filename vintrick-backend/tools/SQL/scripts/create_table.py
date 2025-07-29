# vintrick-backend/vintrick-backend/Tools/SQL/

import pyodbc

def execute_sql_query(server, database, username, password, query):
    """
    Executes a given SQL query on the specified SQL Server database.

    :param server: SQL Server name
    :param database: Database name
    :param username: Username for authentication
    :param password: Password for authentication
    :param query: SQL query to execute
    """
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    try:
        with pyodbc.connect(connection_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                print("Query executed successfully.")
    except pyodbc.Error as e:
        print("Error while executing SQL query:", e)