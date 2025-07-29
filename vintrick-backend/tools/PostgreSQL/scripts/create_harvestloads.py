# ---- create_harvestloads.py
# ---- python tools/PostgreSQL/scripts/create_harvestloads.py
# ---- This script creates the harvestloads table in a PostgreSQL database using a schema file.



from create_table_postgres import execute_sql_query
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

# Load the SQL schema from the file
with open('tools/PostgreSQL/schemas/harvestloads_schema_postgres.sql', 'r') as file:
    create_table_query = file.read()

# Execute the query
execute_sql_query(server, database, username, password, port, create_table_query)