# vintrick-backend/app/api/routes/trans_sum.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.trans_sum import TransSumCreate, TransSumOut
from app.crud import trans_sum as trans_sum_crud
from app.api.deps import get_db
from app.vintrace_api import get_vintrace_api

router = APIRouter()

@router.get("/trans_sum/", response_model=dict)
def list_trans_sums(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, gt=0),
    db: Session = Depends(get_db)
):
    items, total = trans_sum_crud.get_all_trans_sums(db, skip=skip, limit=limit)
    return {
        "items": [TransSumOut.model_validate(item) for item in items],
        "total": total
    }

@router.post("/trans_sum/", response_model=TransSumOut)
def create_trans_sum(
    payload: TransSumCreate, db: Session = Depends(get_db)
):
    try:
        return trans_sum_crud.create_trans_sum(db, payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/trans_sum/{uid}", response_model=TransSumOut)
def read_trans_sum(uid: str, db: Session = Depends(get_db)):
    db_obj = trans_sum_crud.get_trans_sum_by_uid(db, uid)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="TransSum not found")
    return db_obj

@router.patch("/trans_sum/{uid}", response_model=TransSumOut)
def update_trans_sum(
    uid: str, payload: TransSumCreate, db: Session = Depends(get_db)
):
    db_obj = trans_sum_crud.update_trans_sum(db, uid, payload)
    if not db_obj:
        raise HTTPException(status_code=404, detail="TransSum not found")
    return db_obj

@router.delete("/trans_sum/{uid}")
def delete_trans_sum(uid: str, db: Session = Depends(get_db)):
    deleted = trans_sum_crud.delete_trans_sum(db, uid)
    if not deleted:
        raise HTTPException(status_code=404, detail="TransSum not found")
    return {"ok": True}

@router.post("/trans_sum/upload_from_vintrace/", response_model=dict)
def upload_from_vintrace(
    db: Session = Depends(get_db),
    limit: int = Query(20, gt=0),
    offset: int = Query(0, ge=0),
):
    vintrace_api = get_vintrace_api()
    try:
        vintrace_data = vintrace_api["get_transaction_summaries"](limit=limit, offset=offset)
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
            "uploaded_count": len(uploaded),
            "uploaded_ids": uploaded,
            "errors": errors,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Vintrace integration error: {e}")