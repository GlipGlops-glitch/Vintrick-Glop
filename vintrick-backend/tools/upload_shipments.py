# vintrick-backend/tools/SQL/scripts/upload_shipments.py
# Usage: python tools/upload_shipments.py
# Description: Loads and flattens shipment data from tools/data/shipments/all_shipments.json and inserts into the shipments table in SQL Server.

import os
import json
import pyodbc
from dotenv import load_dotenv

# Import the extractor function
from extract_shipment_flat import extract_flat_shipment

load_dotenv()

# Build connection string
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
driver = os.getenv('DB_DRIVER', 'ODBC Driver 18 for SQL Server')
encrypt = os.getenv('DB_ENCRYPT', 'yes')
trust_cert = os.getenv('DB_TRUST_SERVER_CERTIFICATE', 'yes')

conn_str = (
    f"DRIVER={{{driver}}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt={encrypt};"
    f"TrustServerCertificate={trust_cert};"
)

# Load shipments data
with open("tools/data/shipments/all_shipments.json", "r", encoding="utf-8") as f:
    shipments = json.load(f)

# Open connection
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

for shipment in shipments:
    flat = extract_flat_shipment(shipment)  # <- flatten each shipment

    cursor.execute("""
        INSERT INTO shipments (
            id, work_order_number, job_number, shipment_number, type,
            source_id, source_name, source_business_unit,
            destination_winery_id, destination_winery_name, destination_winery_business_unit,
            destination_party_id, destination_party_name, destination_party_extId,
            occurred_time, modified_time,
            carrier_id, carrier_name, carrier_extId,
            reference, dispatch_type_id, dispatch_type_name,
            freight_code_id, freight_code_name,
            reversed, last_modified, synced,
            wine_details, wine_allocations, wine_metrics
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        flat.get("id"),
        flat.get("workOrderNumber"),
        flat.get("jobNumber"),
        flat.get("shipmentNumber"),
        flat.get("type"),
        flat.get("source_id"),
        flat.get("source_name"),
        flat.get("source_businessUnit"),
        flat.get("destination_winery_id"),
        flat.get("destination_winery_name"),
        flat.get("destination_winery_businessUnit"),
        flat.get("destination_party_id"),
        flat.get("destination_party_name"),
        flat.get("destination_party_extId"),
        flat.get("occurredTime"),
        flat.get("modifiedTime"),
        flat.get("carrier_id"),
        flat.get("carrier_name"),
        flat.get("carrier_extId"),
        flat.get("reference"),
        flat.get("dispatchType_id"),
        flat.get("dispatchType_name"),
        flat.get("freightCode_id"),
        flat.get("freightCode_name"),
        flat.get("reversed"),
        flat.get("last_modified"),
        flat.get("synced"),
        flat.get("wineDetails"),
        flat.get("wine_allocations"),
        flat.get("wine_metrics"),
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Shipments uploaded directly to database.")