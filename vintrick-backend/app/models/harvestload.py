# vintrick-backend/app/models/harvestload.py

from sqlalchemy import Column, String, Float, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.core.db import Base
import uuid

class HarvestLoad(Base):
    __tablename__ = "harvestloads"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Vintrace_ST = Column(String, nullable=True)
    Block = Column(String, nullable=True)
    Tons = Column(Float, nullable=True)
    Press = Column(String, nullable=True)
    Tank = Column(String, nullable=True)
    WO = Column(String, nullable=True)
    Date_Received = Column(String, nullable=True)
    AgCode_ST = Column(String, nullable=True)
    Time_Received = Column(String, nullable=True)
    Wine_Type = Column(String, nullable=True)
    Est_Tons_1 = Column(Float, nullable=True)
    Est_Tons_2 = Column(Float, nullable=True)
    Est_Tons_3 = Column(Float, nullable=True)
    Press_Pick_2 = Column(String, nullable=True)
    Linked = Column(String, nullable=True)
    Crush_Pad = Column(String, nullable=True)
    Status = Column(String, nullable=True)
    last_modified = Column(DateTime, nullable=True)
    synced = Column(Boolean, default=False, nullable=True)

    def __repr__(self):
        return f"<harvestload uid={self.uid} vintrace_st={self.Vintrace_ST} tons={self.Tons}>"
