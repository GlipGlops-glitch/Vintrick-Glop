# vintrick-backend/app/api/routes/vintrace_api.py

from fastapi import APIRouter, BackgroundTasks, Query, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.crud.harvestload import get_harvestload_by_uid, create_harvestload, update_harvestload
from app.schemas.harvestload import HarvestLoadCreate
from typing import List
from datetime import datetime, timedelta
import requests  # Or use your Vintrace client

router = APIRouter()

# Dummy function - replace with real Vintrace API call
def fetch_vintrace_data_for_date(date_str: str) -> List[dict]:
    # result = requests.get(...)  # Your actual API call here
    # return result.json()
    return [
        {
            "Vintrace_ST": f"VT-{date_str}-1",
            "Block": "A1",
            "Tons": 1.0,
            "Date_Received": date_str,
            # ...add all required fields...
        }
    ]

def upsert_harvestloads(db: Session, records: List[dict]):
    for rec in records:
        vintrace_st = rec.get("Vintrace_ST")
        existing = db.query(HarvestLoad).filter_by(Vintrace_ST=vintrace_st).first()
        schema_obj = HarvestLoadCreate(**rec)
        if existing:
            update_harvestload(db, existing.uid, schema_obj)
        else:
            create_harvestload(db, schema_obj)

def fetch_and_update_task(start_date: str, end_date: str, db: Session):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    for i in range((end - start).days + 1):
        date_str = (start + timedelta(days=i)).strftime("%Y-%m-%d")
        records = fetch_vintrace_data_for_date(date_str)
        upsert_harvestloads(db, records)

@router.post("/fetch_and_update")
def fetch_and_update(
    start_date: str = Query(...),
    end_date: str = Query(...),
    background_tasks: BackgroundTasks = Depends(),
    db: Session = Depends(get_db),
):
    # Run in background so API returns quickly
    background_tasks.add_task(fetch_and_update_task, start_date, end_date, db)
    return {"status": "Started fetching and updating Vintrace data", "dates": [start_date, end_date]}