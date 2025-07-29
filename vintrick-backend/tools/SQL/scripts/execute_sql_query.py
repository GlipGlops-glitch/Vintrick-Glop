
import pyodbc

def execute_sql_query(database_url, query):
    """
    Executes a given SQL query on the SQL Server database using a connection URL.

    :param database_url: The full ODBC connection string for authentication
    :param query: SQL query to execute
    """
    try:
        with pyodbc.connect(database_url) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                print("Query executed successfully.")
    except pyodbc.Error as e:
        print("Error while executing SQL query:", e)