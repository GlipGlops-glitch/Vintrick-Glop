# vintrick-backend/app/crud/trans_sum.py

from sqlalchemy.orm import Session
from app.models.trans_sum import TransSum
from app.schemas.trans_sum import TransSumCreate
from typing import Optional, List
from datetime import datetime, timezone

def create_trans_sum(db: Session, trans_sum: TransSumCreate) -> TransSum:
    data = trans_sum.model_dump()
    data["last_modified"] = datetime.now(timezone.utc)
    db_obj = TransSum(**data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_all_trans_sums(db: Session, skip: int = 0, limit: int = 50):
    query = db.query(TransSum).order_by(TransSum.last_modified.desc(), TransSum.uid.desc())
    total = query.count()
    if skip:
        query = query.offset(skip)
    if limit:
        query = query.limit(limit)
    return query.all(), total

def get_trans_sum_by_uid(db: Session, uid: str) -> Optional[TransSum]:
    return db.query(TransSum).filter(TransSum.uid == uid).first()

def update_trans_sum(db: Session, uid: str, updates: TransSumCreate) -> Optional[TransSum]:
    db_obj = get_trans_sum_by_uid(db, uid)
    if db_obj is None:
        return None
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db_obj.last_modified = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_trans_sum(db: Session, uid: str) -> bool:
    db_obj = get_trans_sum_by_uid(db, uid)
    if db_obj:
        db.delete(db_obj)
        db.commit()
        return True
    return False