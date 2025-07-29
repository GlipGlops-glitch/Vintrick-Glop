# vintrick-backend/Tools/upload_harvest_loads.py     python Tools/upload_harvest_loads.py    docker-compose exec api python Tools/upload_harvest_loads.py


import pandas as pd
import requests
import uuid
from datetime import datetime, timezone
import time
import os

# Configuration
API_URL = os.getenv("API_URL", "http://localhost:3000/api/harvestloads")
EXCEL_PATH = os.getenv("EXCEL_PATH", "Tools/harvest Loads.xlsx")

# Load Excel data
df = pd.read_excel(EXCEL_PATH).fillna("")

for idx, row in df.iterrows():
    data = {
        "uid": str(uuid.uuid4()),
        "Vintrace_ST": str(row.get("Vintrace ST", "")),
        "Block": str(row.get("Block", "")),
        "Tons": float(row.get("Tons", 0.0) or 0.0),
        "Press": str(row.get("Press", "")),
        "Tank": str(row.get("Tank", "")),
        "WO": str(row.get("WO", "")),
        "Date_Received": str(row.get("Date Received", "")),
        "AgCode_ST": str(row.get("AgCode_ST", "")),
        "Time_Received": str(row.get("Time Received", "")),
        "Wine_Type": str(row.get("Wine Type", "")),
        "Est_Tons_1": float(row.get("Est_Tons_1", 0.0) or 0.0),
        "Est_Tons_2": float(row.get("Est_Tons_2", 0.0) or 0.0),
        "Est_Tons_3": float(row.get("Est_Tons_3", 0.0) or 0.0),
        "Press_Pick_2": str(row.get("Press_Pick_2", "")),
        "Linked": str(row.get("Linked", "")),
        "Crush_Pad": str(row.get("Crush Pad", "")),
        "Status": str(row.get("Status", "")),
        "last_modified": datetime.now(timezone.utc).isoformat(),
        "synced": False,
    }

    try:
        response = requests.post(API_URL, json=data)
        if response.status_code not in (200, 201):
            print(f"Failed at row {idx}: {response.text}")
        else:
            print(f"Uploaded row {idx+1}/{len(df)}")
    except Exception as e:
        print(f"Error at row {idx}: {e}")
    time.sleep(0.05)

print("All done!")
