# vintrick-backend/app/crud/trans_sum.py

from sqlalchemy.orm import Session
from app.models.trans_sum import TransSum
from app.schemas.trans_sum import TransSumCreate
from typing import Optional, List

def create_trans_sum(db: Session, ts: TransSumCreate) -> TransSum:
    data = ts.model_dump()
    db_obj = TransSum(**data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_all_trans_sums(db: Session, skip: int = 0, limit: int = 50):
    query = db.query(TransSum).order_by(TransSum.id.desc())
    total = query.count()
    if skip:
        query = query.offset(skip)
    if limit:
        query = query.limit(limit)
    return query.all(), total

def get_trans_sum_by_id(db: Session, id: int) -> Optional[TransSum]:
    return db.query(TransSum).filter(TransSum.id == id).first()

def delete_trans_sum(db: Session, id: int) -> bool:
    db_obj = get_trans_sum_by_id(db, id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
        return True
    return False