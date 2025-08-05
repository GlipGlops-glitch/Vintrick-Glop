# vintrick-backend/app/schemas/shipment.py

from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class ShipmentBase(BaseModel):
    work_order_number: Optional[str] = None
    job_number: Optional[str] = None
    shipment_number: Optional[str] = None
    type: Optional[str] = None
    source_name: Optional[str] = None
    source_business_unit: Optional[str] = None
    destination_name: Optional[str] = None
    occurred_time: Optional[int] = None
    modified_time: Optional[int] = None
    carrier_name: Optional[str] = None
    carrier_ext_id: Optional[str] = None
    reference: Optional[str] = None
    dispatch_type_name: Optional[str] = None
    freight_code_name: Optional[str] = None
    reversed: Optional[bool] = None
    synced: Optional[bool] = None

class ShipmentCreate(ShipmentBase):
    pass

class ShipmentOut(ShipmentBase):
    uid: UUID

    class Config:
        from_attributes = True