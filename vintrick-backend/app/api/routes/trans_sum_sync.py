# vintrick-backend/app/api/routes/trans_sum_sync.py

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.api.deps import get_db
from typing import List
import os
from datetime import datetime, timedelta

# Replace with your actual Vintrace client path/module!
from app.utils.vintrace_client import VintraceSmartClient
from app.crud import trans_sum  # You will need to implement this CRUD file
from app.schemas.trans_sum import TransSumCreate, TransSumOut  # You will need to implement this schema

router = APIRouter()

@router.post("/vintrace/pull-transactions/", response_model=List[TransSumOut])
def pull_transactions(
    start_date: str = Body(..., embed=True),
    end_date: str = Body(..., embed=True),
    db: Session = Depends(get_db)
):
    # Initialize Vintrace client
    client = VintraceSmartClient(
        api_key=os.getenv("VINTRACE_API_TOKEN"),
        endpoint_map_path=os.getenv("VINTRACE_ENDPOINT_MAP_PATH")
    )

    endpoint_key = "GET:/transaction/search"
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    transactions_saved = []

    for i in range((end - start).days + 1):
        day = (start + timedelta(days=i)).strftime("%Y-%m-%d")
        params = {"startDate": day}
        try:
            transactions = client.call_endpoint(endpoint_key, params=params)
            for tx in transactions.get("transactionSummaries", []):
                # Map fields from Vintrace to TransSumCreate here
                tx_payload = map_vintrace_to_trans_sum(tx)
                db_obj = trans_sum.create_trans_sum(db, TransSumCreate(**tx_payload))
                transactions_saved.append(TransSumOut.model_validate(db_obj))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error on {day}: {e}")
    return transactions_saved

def map_vintrace_to_trans_sum(tx: dict) -> dict:
    # Fill this out based on your TransSum model and schema!
    return {
        "formattedDate": tx.get("formattedDate"),
        "date": tx.get("date"),
        "operationId": tx.get("operationId"),
        "operationTypeId": tx.get("operationTypeId"),
        "operationTypeName": tx.get("operationTypeName"),
        "subOperationTypeId": tx.get("subOperationTypeId"),
        "subOperationTypeName": tx.get("subOperationTypeName"),
        "workorder": tx.get("workorder"),
        "jobNumber": tx.get("jobNumber"),
        "treatment": tx.get("treatment"),
        "assignedBy": tx.get("assignedBy"),
        "completedBy": tx.get("completedBy"),
        "winery": tx.get("winery"),
        "additionalDetails": tx.get("additionalDetails"),
        # If you want to handle nested vessels/loss/addition/analysis, add mapping here!
    }