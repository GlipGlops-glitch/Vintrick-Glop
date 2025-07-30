import uuid
from sqlalchemy import Column, String, Float, DateTime, Boolean
from app.core.db import Base

class HarvestLoad(Base):
    __tablename__ = "harvestloads"

    uid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    Vintrace_ST = Column(String(50), nullable=True)
    Block = Column(String(50), nullable=True)
    Tons = Column(Float, nullable=True, default=0.0)
    Press = Column(String(50), nullable=True)
    Tank = Column(String(50), nullable=True)
    WO = Column(String(50), nullable=True)
    Date_Received = Column(String(50), nullable=True)  # Change to Date if you want dates!
    AgCode_ST = Column(String(50), nullable=True)
    Time_Received = Column(String(50), nullable=True)
    Wine_Type = Column(String(50), nullable=True)
    Est_Tons_1 = Column(Float, nullable=True, default=0.0)
    Est_Tons_2 = Column(Float, nullable=True, default=0.0)
    Est_Tons_3 = Column(Float, nullable=True, default=0.0)
    Press_Pick_2 = Column(String(50), nullable=True)
    Linked = Column(String(10), nullable=True)
    Crush_Pad = Column(String(50), nullable=True)
    Status = Column(String(50), nullable=True)
    last_modified = Column(DateTime, nullable=False)
    synced = Column(Boolean, default=False)


from sqlalchemy import Column, String, Float, Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from app.core.db import Base
import uuid

class HarvestLoad(Base):
    __tablename__ = "harvestloads"

    uid = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4, index=True)
    Vintrace_ST = Column(String)
    Block = Column(String)
    Tons = Column(Float)
    Press = Column(String)
    Tank = Column(String)
    WO = Column(String)
    Date_Received = Column(String)
    AgCode_ST = Column(String)
    Time_Received = Column(String)
    Wine_Type = Column(String)
    Est_Tons_1 = Column(Float)
    Est_Tons_2 = Column(Float)
    Est_Tons_3 = Column(Float)
    Press_Pick_2 = Column(String)
    Linked = Column(String)
    Crush_Pad = Column(String)
    Status = Column(String)
    last_modified = Column(DateTime)
    synced = Column(Boolean, default=False)

    def __repr__(self):
        return f"<HarvestLoad uid={self.uid} Vintrace_ST={self.Vintrace_ST} Tons={self.Tons}>"