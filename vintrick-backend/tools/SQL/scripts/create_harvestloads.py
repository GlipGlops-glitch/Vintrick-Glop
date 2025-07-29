# filepath: /c:/Users/cah01/Code/Vintrick/SQL/create_harvestloads.py
from create_table import execute_sql_query
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection details from .env
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

# Load the SQL schema from the file
with open('schemas/harvestloads_schema.sql', 'r') as file:
    create_table_query = file.read()

# Execute the query
execute_sql_query(server, database, username, password, create_table_query)