# vintrick-backend/app/api/routes/vintrace_pull.py

from fastapi import APIRouter, Depends, HTTPException, Query, Body
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.vintrace_api import get_vintrace_api
from app.schemas.trans_sum import TransSumCreate
from app.crud import trans_sum as trans_sum_crud
import subprocess
import sys
import os
import json

router = APIRouter()

@router.post("/vintrace/run-trans-fetch/", tags=["vintrace"])
def run_trans_fetch(
    dateFrom: str = Query(...),
    dateTo: str = Query(...),
    ownerName: str = Query(None),
    batchName: str = Query(None),
    wineryName: str = Query(None),
    max_workers: int = Query(1)
):
    """
    Runs transFetch.py in tools with parameters from the API call.
    Returns its output or error. (Legacy fetcher)
    """
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../tools/transFetch.py"))
    param_dict = {
        "dateFrom": dateFrom,
        "dateTo": dateTo,
        "ownerName": ownerName,
        "batchName": batchName,
        "wineryName": wineryName,
        "max_workers": max_workers
    }
    param_dict = {k: v for k, v in param_dict.items() if v is not None}
    param_json = json.dumps(param_dict)
    try:
        result = subprocess.run(
            [sys.executable, script_path, param_json],
            capture_output=True,
            text=True,
            check=True
        )
        return {
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "stdout": e.stdout,
            "stderr": e.stderr,
            "returncode": e.returncode
        }
    except Exception as ex:
        return {
            "status": "error",
            "error": str(ex)
        }

@router.post("/pull-transactions/", tags=["vintrace"])
def pull_transactions_from_vintrace(
    start_date: str = Body(...),
    end_date: str = Body(...),
    db: Session = Depends(get_db)
):
    """
    Fetches transactions from Vintrace using the REST API and uploads them to SQL DB.
    """
    vintrace_api = get_vintrace_api()
    try:
        # Pass date filters to Vintrace API
        vintrace_data = vintrace_api["get_transaction_summaries"](start_date=start_date, end_date=end_date)
        results = vintrace_data.get("results", [])
        uploaded = []
        errors = []
        for rec in results:
            try:
                payload = TransSumCreate(**rec)
                db_obj = trans_sum_crud.create_trans_sum(db, payload)
                uploaded.append(str(getattr(db_obj, "operation_id", getattr(db_obj, "id", None))) or "unknown")
            except Exception as e:
                errors.append({"record": rec, "error": str(e)})
        return {
            "start_date": start_date,
            "end_date": end_date,
            "uploaded_count": len(uploaded),
            "uploaded_ids": uploaded,
            "errors": errors,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Vintrace integration error: {e}")