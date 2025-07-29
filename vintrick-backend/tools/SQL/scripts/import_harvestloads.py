# python tools/SQL/scripts/import_harvestloads.py

import pandas as pd
import pyodbc
from dotenv import load_dotenv
import os
import uuid
from datetime import datetime, timezone

def safe_float(val):
    """Convert to float, return 0.0 if conversion fails or value is missing."""
    try:
        if pd.isnull(val) or val == "" or val is None:
            return 0.0
        return float(val)
    except Exception:
        return 0.0

def safe_str(val):
    """Convert to string, return empty string if value is missing or NaN."""
    if pd.isnull(val) or val is None:
        return ""
    return str(val)

def safe_bool(val):
    """Convert to bool, treat any non-true value as False."""
    return bool(val) if not pd.isnull(val) else False

# Load environment variables
load_dotenv()
database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise ValueError("DATABASE_URL not found in .env")

# Mapping from Excel columns to SQL columns
excel_to_sql = {
    "Vintrace ST": "Vintrace_ST",
    "Block": "Block",
    "Tons": "Tons",
    "Press": "Press",
    "Tank": "Tank",
    "WO": "WO",
    "Date Received": "Date_Received",
    "AgCode_ST": "AgCode_ST",
    "Time Received": "Time_Received",
    "Wine Type": "Wine_Type",
    "Est_Tons_1": "Est_Tons_1",
    "Est_Tons_2": "Est_Tons_2",
    "Est_Tons_3": "Est_Tons_3",
    "Press_Pick_2": "Press_Pick_2",
    "Linked": "Linked",
    "Crush Pad": "Crush_Pad",
    "Status": "Status"
}

# Read Excel file (change the filename/path if needed)
df = pd.read_excel('tools/SQL/data/harvestLoads.xlsx')

with pyodbc.connect(database_url) as conn:
    cursor = conn.cursor()
    for idx, row in df.iterrows():
        data = {
            "uid": str(uuid.uuid4()),
            "last_modified": datetime.now(timezone.utc),
            "synced": False
        }
        for excel_col, sql_col in excel_to_sql.items():
            value = row.get(excel_col, "")
            # Handle numeric (float) columns
            if sql_col in ["Tons", "Est_Tons_1", "Est_Tons_2", "Est_Tons_3"]:
                data[sql_col] = safe_float(value)
            # All other columns are strings in your model
            else:
                data[sql_col] = safe_str(value)

        cursor.execute("""
            INSERT INTO harvestloads (
                uid, Vintrace_ST, Block, Tons, Press, Tank, WO, Date_Received,
                AgCode_ST, Time_Received, Wine_Type, Est_Tons_1, Est_Tons_2,
                Est_Tons_3, Press_Pick_2, Linked, Crush_Pad, Status, last_modified, synced
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["uid"],
            data["Vintrace_ST"],
            data["Block"],
            data["Tons"],
            data["Press"],
            data["Tank"],
            data["WO"],
            data["Date_Received"],
            data["AgCode_ST"],
            data["Time_Received"],
            data["Wine_Type"],
            data["Est_Tons_1"],
            data["Est_Tons_2"],
            data["Est_Tons_3"],
            data["Press_Pick_2"],
            data["Linked"],
            data["Crush_Pad"],
            data["Status"],
            data["last_modified"],
            data["synced"],
        ))
    conn.commit()
print("Data import complete!")