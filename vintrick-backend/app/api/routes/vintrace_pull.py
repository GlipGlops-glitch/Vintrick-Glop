# vintrick-backend/app/api/routes/vintrace_pull.py

from fastapi import APIRouter, Query
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
    Returns its output or error.
    """
    # Absolute path to transFetch.py
  # vintrick-backend/app/api/routes/vintrace_pull.py
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../tools/transFetch.py"))

    # Prepare parameters as a JSON string for the legacy fetcher
    param_dict = {
        "dateFrom": dateFrom,
        "dateTo": dateTo,
        "ownerName": ownerName,
        "batchName": batchName,
        "wineryName": wineryName,
        "max_workers": max_workers
    }
    # Remove None values so they aren't passed as "null"
    param_dict = {k: v for k, v in param_dict.items() if v is not None}

    # Pass parameters as a JSON string argument
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