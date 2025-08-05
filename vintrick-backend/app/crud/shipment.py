# vintrick-backend/app/crud/shipment.py

from sqlalchemy.orm import Session
from app.models.shipment import Shipment
from app.schemas.shipment import ShipmentCreate
from typing import Optional
from datetime import datetime, timezone

def create_shipment(db: Session, shipment: ShipmentCreate) -> Shipment:
    data = shipment.model_dump()
    data["last_modified"] = datetime.now(timezone.utc)
    db_obj = Shipment(**data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_all_shipments(db: Session, skip: int = 0, limit: int = 50):
    query = db.query(Shipment).order_by(Shipment.modified_time.desc(), Shipment.uid.desc())
    total = query.count()
    if skip:
        query = query.offset(skip)
    if limit:
        query = query.limit(limit)
    return query.all(), total

def get_shipment_by_uid(db: Session, uid: str) -> Optional[Shipment]:
    return db.query(Shipment).filter(Shipment.uid == uid).first()