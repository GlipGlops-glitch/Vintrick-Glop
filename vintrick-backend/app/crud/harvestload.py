# vintrick-backend/crud/harvestload.py

from sqlalchemy.orm import Session
from app.models.harvestload import HarvestLoad
from app.schemas.harvestload import HarvestLoadCreate


def create_harvestload(db: Session, harvestload: HarvestLoadCreate):
    db_obj = HarvestLoad(**harvestload.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_all_harvestloads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(HarvestLoad).offset(skip).limit(limit).all()


def get_harvestload_by_uid(db: Session, uid: str):
    return db.query(HarvestLoad).filter(HarvestLoad.uid == uid).first()


def delete_harvestload(db: Session, uid: str):
    obj = get_harvestload_by_uid(db, uid)
    if obj:
        db.delete(obj)
        db.commit()
    return obj
