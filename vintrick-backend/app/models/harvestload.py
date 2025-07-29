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