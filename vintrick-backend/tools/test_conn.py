import os
import pyodbc
from urllib.parse import urlparse, parse_qs, unquote

from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url and database_url.startswith("mssql+pyodbc://"):
    # Parse the URL
    url = urlparse(database_url)
    user = url.username
    password = url.password
    server = url.hostname
    db = url.path.lstrip('/')
    query = parse_qs(url.query)
    driver = unquote(query.get('driver', ['ODBC Driver 18 for SQL Server'])[0])
    encrypt = query.get('Encrypt', ['yes'])[0]
    trust_cert = query.get('TrustServerCertificate', ['yes'])[0]

    conn_str = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={db};"
        f"UID={user};"
        f"PWD={password};"
        f"Encrypt={encrypt};"
        f"TrustServerCertificate={trust_cert};"
    )
else:
    raise RuntimeError("No valid DATABASE_URL found!")

print("Using ODBC connection string:")
print(conn_str)

try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)