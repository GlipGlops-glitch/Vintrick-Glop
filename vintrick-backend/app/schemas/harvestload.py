# vintrick-backend/app/schemas/harvestload.py

from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class HarvestLoadBase(BaseModel):
    Vintrace_ST: Optional[str] = None
    Block: Optional[str] = None
    Tons: Optional[float] = None
    Press: Optional[str] = None
    Tank: Optional[str] = None
    WO: Optional[str] = None
    Date_Received: Optional[str] = None
    AgCode_ST: Optional[str] = None
    Time_Received: Optional[str] = None
    Wine_Type: Optional[str] = None
    Est_Tons_1: Optional[float] = None
    Est_Tons_2: Optional[float] = None
    Est_Tons_3: Optional[float] = None
    Press_Pick_2: Optional[str] = None
    Linked: Optional[str] = None
    Crush_Pad: Optional[str] = None
    Status: Optional[str] = None
    synced: Optional[bool] = None
    
    # Removed since it will be auto
    #last_modified: Optional[datetime] = None

class HarvestLoadCreate(HarvestLoadBase):
    pass

class HarvestLoadOut(HarvestLoadBase):
    uid: UUID

    class Config:
        from_attributes = True