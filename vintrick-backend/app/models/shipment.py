# vintrick-backend/app/models/shipment.py

import uuid
from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean
from app.core.db import Base

class Shipment(Base):
    __tablename__ = "shipments"

    uid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    work_order_number = Column(String(50), nullable=True)
    job_number = Column(String(50), nullable=True)
    shipment_number = Column(String(50), nullable=True)
    type = Column(String(50), nullable=True)
    source_name = Column(String(100), nullable=True)
    source_business_unit = Column(String(100), nullable=True)
    destination_name = Column(String(100), nullable=True)
    occurred_time = Column(Integer, nullable=True)  # epoch ms
    modified_time = Column(Integer, nullable=True)
    carrier_name = Column(String(100), nullable=True)
    carrier_ext_id = Column(String(100), nullable=True)
    reference = Column(String(100), nullable=True)
    dispatch_type_name = Column(String(100), nullable=True)
    freight_code_name = Column(String(50), nullable=True)
    reversed = Column(Boolean, default=False)
    last_modified = Column(DateTime, nullable=False)
    synced = Column(Boolean, default=False)
    # Add wineDetails and other objects as separate tables or JSON columns if needed