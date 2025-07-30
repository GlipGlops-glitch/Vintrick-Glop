import os
import pyodbc
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Try to get the connection string from the environment variable
conn_str = os.getenv("DB_CONN_STR")

if not conn_str:
    # Fallback: try to build from DATABASE_URL if present (pyodbc format is different from SQLAlchemy!)
    database_url = os.getenv("DATABASE_URL")
    if database_url and database_url.startswith("mssql+pyodbc://"):
        # Basic parse (NOTE: for simple cases only)
        import re
        match = re.match(
            r"mssql\+pyodbc://(?P<user>.*?):(?P<pw>.*?)@(?P<server>.*?)/(?P<db>.*?)\?driver=(?P<driver>.+)",
            database_url
        )
        if match:
            d = match.groupdict()
            conn_str = (
                f"DRIVER={{{d['driver'].replace('+', ' ')}}};"
                f"SERVER={d['server']};"
                f"DATABASE={d['db']};"
                f"UID={d['user']};"
                f"PWD={d['pw']};"
                "Encrypt=yes;"
                "TrustServerCertificate=yes;"
            )

if not conn_str:
    raise RuntimeError(
        "No connection string found! Please set DB_CONN_STR or DATABASE_URL in your .env file."
    )

try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)