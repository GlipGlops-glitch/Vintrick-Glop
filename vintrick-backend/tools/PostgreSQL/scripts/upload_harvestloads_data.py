# ---- upload_harvestloads_data.py
# ---- python tools/PostgreSQL/scripts/upload_harvestloads_data.py
# ---- This script uploads initial data from an Excel file into the harvestloads table.

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os
import uuid
from datetime import datetime, timezone

# Load environment variables from .env file
load_dotenv()

# Database connection details from .env
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT', 5432)  # Default PostgreSQL port

# Path to the Excel file
EXCEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'harvestloads.xlsx')  # Update with the actual path to your Excel file

def upload_data_to_harvestloads():
    """
    Reads data from an Excel file and uploads it to the harvestloads table in PostgreSQL.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(EXCEL_PATH).fillna("")

        # Prepare the data for insertion
        rows = []
        for _, row in df.iterrows():
            rows.append((
                str(uuid.uuid4()),  # uid
                str(row.get("Vintrace ST", "")),
                str(row.get("Block", "")),
                float(row.get("Tons", 0.0) or 0.0),
                str(row.get("Press", "")),
                str(row.get("Tank", "")),
                str(row.get("WO", "")),
                str(row.get("Date Received", "")),
                str(row.get("AgCode_ST", "")),
                str(row.get("Time Received", "")),
                str(row.get("Wine Type", "")),
                float(row.get("Est_Tons_1", 0.0) or 0.0),
                float(row.get("Est_Tons_2", 0.0) or 0.0),
                float(row.get("Est_Tons_3", 0.0) or 0.0),
                str(row.get("Press_Pick_2", "")),
                str(row.get("Linked", "")),
                str(row.get("Crush Pad", "")),
                str(row.get("Status", "")),
                datetime.now(timezone.utc),  # last_modified
                False  # synced
            ))

        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=server,
            database=database,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()

        # Insert data into the harvestloads table
        insert_query = """
        INSERT INTO harvestloads (
            uid, Vintrace_ST, Block, Tons, Press, Tank, WO, Date_Received, AgCode_ST,
            Time_Received, Wine_Type, Est_Tons_1, Est_Tons_2, Est_Tons_3, Press_Pick_2,
            Linked, Crush_Pad, Status, last_modified, synced
        ) VALUES %s
        """
        execute_values(cursor, insert_query, rows)
        connection.commit()
        print(f"Successfully uploaded {len(rows)} rows to the harvestloads table.")

    except Exception as e:
        print("Error while uploading data:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    upload_data_to_harvestloads()