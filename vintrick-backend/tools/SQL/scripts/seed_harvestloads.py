# python tools/SQL/scripts/seed_harvestloads.py

# cd C:\Users\cah01\Code\Vintrick\vintrick-backend
# python -m tools.SQL.scripts.seed_harvestloads

import os
import uuid
from datetime import datetime, timezone

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# --- Adjust these imports to your actual project structure!
# Base and HarvestLoad model must be correct.
from app.core.db import Base  # Your declarative_base
from app.models.harvestload import HarvestLoad

# 1. Load environment variables
load_dotenv()
database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise ValueError("DATABASE_URL not found in .env")

# 2. Set up SQLAlchemy engine and session
engine = create_engine(database_url, echo=True)
# Creates all tables if they don't exist yet
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)

# 3. Define safe conversion helpers
def safe_float(val):
    try:
        if pd.isnull(val) or val == "" or val is None:
            return 0.0
        return float(val)
    except Exception:
        return 0.0

def safe_str(val):
    if pd.isnull(val) or val is None:
        return ""
    return str(val)

def safe_bool(val):
    return bool(val) if not pd.isnull(val) else False

# 4. Excel to SQL column mapping
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

def seed_data():
    # 5. Read Excel data
    excel_path = 'tools/SQL/data/harvestLoads.xlsx'
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Excel file not found at {excel_path}")

    df = pd.read_excel(excel_path)
    session = SessionLocal()
    try:
        for idx, row in df.iterrows():
            data = {
                "uid": uuid.uuid4(),  # <-- Pass UUID object, not str
                "last_modified": datetime.now(timezone.utc),
                "synced": False
            }
            for excel_col, sql_col in excel_to_sql.items():
                value = row.get(excel_col, "")
                if sql_col in ["Tons", "Est_Tons_1", "Est_Tons_2", "Est_Tons_3"]:
                    data[sql_col] = safe_float(value)
                else:
                    data[sql_col] = safe_str(value)
            obj = HarvestLoad(**data)
            session.add(obj)
        session.commit()
        print("Data seeding complete!")
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
        raise
    finally:
        session.close()

if __name__ == "__main__":
    seed_data()