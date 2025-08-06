# vintrick-backend/tools/SQL/scripts/create_trans_sum.py
# ---  Vintrick/vintrick-backend/Tools/SQL/scripts/create_trans_sum.py
# --- python tools/SQL/scripts/create_trans_sum.py
# ---  This script creates the trans_sum (transaction summary) tables in a SQL Server database using a schema file.

from execute_sql_query import execute_sql_query
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the ODBC/SQLAlchemy database URL from .env (use DB_URL, fallback to DATABASE_URL)
database_url = os.getenv('DB_URL') or os.getenv('DATABASE_URL')

if not database_url:
    raise RuntimeError("No DB_URL or DATABASE_URL found in environment!")

# Load the SQL schema from the file
with open('tools/SQL/schemas/trans_sum_schema.sql', 'r') as file:
    create_table_query = file.read()

# Execute the query using the connection URL
execute_sql_query(database_url, create_table_query)