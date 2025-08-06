# vintrick-backend/app/api/routes/trans_sum.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.trans_sum import TransSumCreate, TransSumOut, TransSumResponse
from app.crud.trans_sum import (
    create_trans_sum,
    get_all_trans_sums,
    get_trans_sum_by_id,
    delete_trans_sum
)
from app.api.deps import get_db

router = APIRouter()

@router.get("/trans_sums/", response_model=TransSumResponse)
def list_trans_sums(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, gt=0),
    db: Session = Depends(get_db)
):
    items, total = get_all_trans_sums(db, skip=skip, limit=limit)
    return {
        "status": "Success",
        "message": None,
        "transactionSummaries": [TransSumOut.model_validate(item) for item in items]
    }

@router.post("/trans_sums/", response_model=TransSumOut)
def create_trans_sum_route(
    trans_sum: TransSumCreate, db: Session = Depends(get_db)
):
    try:
        return create_trans_sum(db, trans_sum)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/trans_sums/{trans_sum_id}", response_model=TransSumOut)
def read_trans_sum(trans_sum_id: int, db: Session = Depends(get_db)):
    db_obj = get_trans_sum_by_id(db, trans_sum_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="TransSum not found")
    return db_obj

@router.delete("/trans_sums/{trans_sum_id}")
def delete_trans_sum_route(trans_sum_id: int, db: Session = Depends(get_db)):
    deleted = delete_trans_sum(db, trans_sum_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="TransSum not found")
    return {"ok": True}