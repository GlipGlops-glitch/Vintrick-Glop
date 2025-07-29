# ---  Vintrick/vintrick-backend/Tools/SQL/scripts/create_harvestloads.py
# --- python tools/SQL/scripts/create_harvestloads.py
# ---  This script creates the harvestloads table in a SQL Server database using a schema file.

from execute_sql_query import execute_sql_query
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database URL from .env
database_url = os.getenv('DATABASE_URL')

# Load the SQL schema from the file (adjust the path if needed)
with open('tools/SQL/schemas/harvestloads_schema.sql', 'r') as file:
    create_table_query = file.read()

# Execute the query using the connection URL
execute_sql_query(database_url, create_table_query)