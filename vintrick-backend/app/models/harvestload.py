from sqlalchemy import Column, String, Float, Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class HarvestLoad(Base):
    __tablename__ = "harvestloads"

    uid = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    Vintrace_ST = Column(String(255))
    Block = Column(String(255))
    Tons = Column(Float)
    Press = Column(String(255))
    Tank = Column(String(255))
    WO = Column(String(255))
    Date_Received = Column(String(50))
    AgCode_ST = Column(String(255))
    Time_Received = Column(String(50))
    Wine_Type = Column(String(255))
    Est_Tons_1 = Column(Float)
    Est_Tons_2 = Column(Float)
    Est_Tons_3 = Column(Float)
    Press_Pick_2 = Column(String(255))
    Linked = Column(String(255))
    Crush_Pad = Column(String(255))
    Status = Column(String(255))
    last_modified = Column(DateTime)
    synced = Column(Boolean, default=False)