# vintrick-backend/app/api/routes/shipments.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.shipment import ShipmentCreate, ShipmentOut
from app.crud import shipment
from app.api.deps import get_db

router = APIRouter()

@router.get("/shipments/", response_model=dict)
def list_shipments(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, gt=0),
    db: Session = Depends(get_db)
):
    items, total = shipment.get_all_shipments(db, skip=skip, limit=limit)
    return {
        "items": [ShipmentOut.model_validate(item) for item in items],
        "total": total
    }

@router.get("/shipments/{shipment_id}", response_model=ShipmentOut)
def read_shipment(shipment_id: str, db: Session = Depends(get_db)):
    db_shipment = shipment.get_shipment_by_uid(db, shipment_id)
    if db_shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return ShipmentOut.model_validate(db_shipment)

@router.post("/shipments/", response_model=ShipmentOut)
def create_shipment(
    shipment_in: ShipmentCreate, db: Session = Depends(get_db)
):
    try:
        return shipment.create_shipment(db, shipment_in)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))