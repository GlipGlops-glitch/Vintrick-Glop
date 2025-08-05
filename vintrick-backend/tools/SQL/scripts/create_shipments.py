# vintrick-backend/tools/SQL/scripts/create_shipments.py
# Usage: python tools/SQL/scripts/create_shipments.py
# This script creates the shipments table in your SQL Server database using a schema file.

from dotenv import load_dotenv
import os
from execute_sql_query import execute_sql_query

# Load environment variables from .env file
load_dotenv()

# Get database URL from environment
database_url = os.getenv('DATABASE_URL')

# Load the SQL schema from the file (adjust path if needed)
with open('tools/SQL/schemas/shipments_schema.sql', 'r') as file:
    create_table_query = file.read()

# Execute the query using the connection URL
execute_sql_query(database_url, create_table_query)