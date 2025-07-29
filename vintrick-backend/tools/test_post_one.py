# vintrick-backend/Tools/test_post_one.py  python Tools/test_post_one.py

import requests
import uuid
from datetime import datetime, timezone

# Single test payload
payload = {
    "uid": str(uuid.uuid4()),
    "Vintrace_ST": "VT-12345",
    "Block": "A1",
    "Tons": 1.5,
    "Press": "P1",
    "Tank": "T2",
    "WO": "W123",
    "Date_Received": "2025-07-26",
    "AgCode_ST": "AG567",
    "Time_Received": "14:30",
    "Wine_Type": "Red",
    "Est_Tons_1": 1.2,
    "Est_Tons_2": 1.3,
    "Est_Tons_3": 1.4,
    "Press_Pick_2": "Y",
    "Linked": "N",
    "Crush_Pad": "Pad A",
    "Status": "Received",
    "last_modified": datetime.now(timezone.utc).isoformat(),
    "synced": False
}

res = requests.post("http://localhost:3000/api/harvestloads", json=payload)

print(f"Status Code: {res.status_code}")
print(f"Response: {res.text}")
