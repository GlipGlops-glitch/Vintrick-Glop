from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.harvestload import HarvestLoad
from app.schemas.harvestload import HarvestLoadCreate
from uuid import UUID
from typing import Optional, List

def get_all_harvestloads(session: Session, skip: int = 0, limit: int = 100) -> list[HarvestLoad]:
    return session.query(HarvestLoad).offset(skip).limit(limit).all()

def get_harvestload_by_uid(session: Session, uid: UUID) -> Optional[HarvestLoad]:
    return session.query(HarvestLoad).filter(HarvestLoad.uid == uid).first()

def create_harvestload(session: Session, load_data: HarvestLoadCreate) -> HarvestLoad:
    load = HarvestLoad(**load_data.dict())
    session.add(load)
    session.commit()
    session.refresh(load)
    return load

def update_harvestload(session: Session, uid: UUID, updates) -> Optional[HarvestLoad]:
    load = get_harvestload_by_uid(session, uid)
    if not load:
        return None

    if isinstance(updates, BaseModel):
        updates = updates.dict()

    for key, value in updates.items():
        setattr(load, key, value)
    session.commit()
    session.refresh(load)
    return load

def delete_harvestload(session: Session, uid: UUID) -> Optional[HarvestLoad]:
    load = get_harvestload_by_uid(session, uid)
    if not load:
        return None
    session.delete(load)
    session.commit()
    return load