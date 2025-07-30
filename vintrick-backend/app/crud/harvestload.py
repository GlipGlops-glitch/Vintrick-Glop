# vintrick-backend/app/crud/harvestload.py

from sqlalchemy.orm import Session
from app.models.harvestload import HarvestLoad
from app.schemas.harvestload import HarvestLoadCreate
from typing import Optional, List
from datetime import datetime, timezone

def create_harvestload(db: Session, harvestload: HarvestLoadCreate) -> HarvestLoad:
    data = harvestload.model_dump()
    data["last_modified"] = datetime.now(timezone.utc)
    db_obj = HarvestLoad(**data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_all_harvestloads(db: Session, skip: int = 0, limit: int = 100) -> List[HarvestLoad]:
    return (
        db.query(HarvestLoad)
        .order_by(HarvestLoad.uid)  # <-- Add this line!
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_harvestload_by_uid(db: Session, uid: str) -> Optional[HarvestLoad]:
    return db.query(HarvestLoad).filter(HarvestLoad.uid == uid).first()

def update_harvestload(db: Session, uid: str, updates: HarvestLoadCreate) -> Optional[HarvestLoad]:
    db_obj = get_harvestload_by_uid(db, uid)
    if db_obj is None:
        return None
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_harvestload(db: Session, uid: str) -> bool:
    db_obj = get_harvestload_by_uid(db, uid)
    if db_obj:
        db.delete(db_obj)
        db.commit()
        return True
    return False

    from datetime import datetime, timezone

