# vintrick-backend/app/dao/harvest_load_dao.py

from sqlalchemy.orm import Session
from app.models.harvestload import HarvestLoad
from app.schemas.harvestload import HarvestLoadCreate

def get_all_harvestloads(db: Session):
    return db.query(HarvestLoad).all()

def get_harvestload_by_uid(db: Session, uid):
    return db.query(HarvestLoad).filter(HarvestLoad.uid == uid).first()

def create_harvestload(db: Session, load: HarvestLoadCreate):
    db_load = HarvestLoad(**load.dict())
    db.add(db_load)
    db.commit()
    db.refresh(db_load)
    return db_load

def delete_harvestload(db: Session, uid):
    db_load = get_harvestload_by_uid(db, uid)
    if db_load:
        db.delete(db_load)
        db.commit()
    return db_load

def update_harvestload(db: Session, uid, updates: dict):
    db_load = get_harvestload_by_uid(db, uid)
    if db_load:
        for key, value in updates.items():
            setattr(db_load, key, value)
        db.commit()
        db.refresh(db_load)
    return db_load
