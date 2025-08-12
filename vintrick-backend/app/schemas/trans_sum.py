# vintrick-backend/app/schemas/trans_sum.py

from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

# VesselDetailsOut matches vessel_details table
class VesselDetailsOut(BaseModel):
    contentsId: Optional[int] = Field(None, alias="contentsId")
    batch: Optional[str] = Field(None, alias="batch")
    batchId: Optional[int] = Field(None, alias="batchId")
    volume: Optional[int] = Field(None, alias="volume")  # INT in SQL
    volumeUnit: Optional[str] = Field(None, alias="volumeUnit")
    dip: Optional[str] = Field(None, alias="dip")
    state: Optional[str] = Field(None, alias="state")
    rawTaxClass: Optional[str] = Field(None, alias="rawTaxClass")
    federalTaxClass: Optional[str] = Field(None, alias="federalTaxClass")
    stateTaxClass: Optional[str] = Field(None, alias="stateTaxClass")
    program: Optional[str] = Field(None, alias="program")

# VesselsOut matches vessels table (used for both fromVessel and toVessel)
class VesselsOut(BaseModel):
    name: Optional[str] = Field(None, alias="name")
    vessel_id: Optional[int] = Field(None, alias="vessel_id")
    beforeDetails: Optional[VesselDetailsOut] = Field(None, alias="beforeDetails")
    afterDetails: Optional[VesselDetailsOut] = Field(None, alias="afterDetails")
    volOut: Optional[int] = Field(None, alias="volOut")  # INT in SQL
    volOutUnit: Optional[str] = Field(None, alias="volOutUnit")
    volIn: Optional[int] = Field(None, alias="volIn")    # INT in SQL
    volInUnit: Optional[str] = Field(None, alias="volInUnit")

class LossDetailsOut(BaseModel):
    volume: Optional[int] = Field(None, alias="volume")  # INT in SQL
    volumeUnit: Optional[str] = Field(None, alias="volumeUnit")
    reason: Optional[str] = Field(None, alias="reason")

class AdditivesOut(BaseModel):
    additive_id: Optional[int] = Field(None, alias="additive_id")
    name: Optional[str] = Field(None, alias="name")
    description: Optional[str] = Field(None, alias="description")

class AdditionOpsOut(BaseModel):
    vesselId: Optional[int] = Field(None, alias="vesselId")
    vesselName: Optional[str] = Field(None, alias="vesselName")
    batchId: Optional[int] = Field(None, alias="batchId")
    batchName: Optional[str] = Field(None, alias="batchName")
    templateId: Optional[int] = Field(None, alias="templateId")
    templateName: Optional[str] = Field(None, alias="templateName")
    changeToState: Optional[str] = Field(None, alias="changeToState")
    volume: Optional[str] = Field(None, alias="volume")
    amount: Optional[float] = Field(None, alias="amount")
    unit: Optional[str] = Field(None, alias="unit")
    lotNumbers: Optional[str] = Field(None, alias="lotNumbers")
    additive: Optional[AdditivesOut] = Field(None, alias="additive")

class MetricAnalysisOut(BaseModel):
    name: Optional[str] = Field(None, alias="name")
    value: Optional[float] = Field(None, alias="value")
    txtValue: Optional[str] = Field(None, alias="txtValue")
    unit: Optional[str] = Field(None, alias="unit")

class AnalysisOpsOut(BaseModel):
    vesselId: Optional[int] = Field(None, alias="vesselId")
    vesselName: Optional[str] = Field(None, alias="vesselName")
    batchId: Optional[int] = Field(None, alias="batchId")
    batchName: Optional[str] = Field(None, alias="batchName")
    templateId: Optional[int] = Field(None, alias="templateId")
    templateName: Optional[str] = Field(None, alias="templateName")
    metrics: Optional[List[MetricAnalysisOut]] = Field(default_factory=list, alias="metrics")

class TransSumOut(BaseModel):
    formattedDate: Optional[str] = Field(None, alias="formattedDate")
    date: Optional[int] = Field(None, alias="date")
    operationId: Optional[int] = Field(None, alias="operationId")
    operationTypeId: Optional[int] = Field(None, alias="operationTypeId")
    operationTypeName: Optional[str] = Field(None, alias="operationTypeName")
    subOperationTypeId: Optional[int] = Field(None, alias="subOperationTypeId")
    subOperationTypeName: Optional[str] = Field(None, alias="subOperationTypeName")
    workorder: Optional[str] = Field(None, alias="workorder")
    jobNumber: Optional[str] = Field(None, alias="jobNumber")
    treatment: Optional[str] = Field(None, alias="treatment")
    assignedBy: Optional[str] = Field(None, alias="assignedBy")
    completedBy: Optional[str] = Field(None, alias="completedBy")
    winery: Optional[str] = Field(None, alias="winery")
    fromVessel: Optional[VesselsOut] = Field(None, alias="fromVessel")
    toVessel: Optional[VesselsOut] = Field(None, alias="toVessel")
    lossDetails: Optional[LossDetailsOut] = Field(None, alias="lossDetails")
    additionOps: Optional[AdditionOpsOut] = Field(None, alias="additionOps")
    analysisOps: Optional[AnalysisOpsOut] = Field(None, alias="analysisOps")
    additionalDetails: Optional[str] = Field(None, alias="additionalDetails")
    # last_modified: Optional[str] = Field(None, alias="last_modified")

    @field_validator('jobNumber', mode='before')
    def coerce_job_number(cls, v):
        if v is not None:
            return str(v)
        return v

    class Config:
        from_attributes = True  # For compatibility with SQLAlchemy models

class TransSumCreate(BaseModel):
    formattedDate: Optional[str] = Field(None, alias="formattedDate")
    date: Optional[int] = Field(None, alias="date")
    operationId: Optional[int] = Field(None, alias="operationId")
    operationTypeId: Optional[int] = Field(None, alias="operationTypeId")
    operationTypeName: Optional[str] = Field(None, alias="operationTypeName")
    subOperationTypeId: Optional[int] = Field(None, alias="subOperationTypeId")
    subOperationTypeName: Optional[str] = Field(None, alias="subOperationTypeName")
    workorder: Optional[str] = Field(None, alias="workorder")
    jobNumber: Optional[str] = Field(None, alias="jobNumber")
    treatment: Optional[str] = Field(None, alias="treatment")
    assignedBy: Optional[str] = Field(None, alias="assignedBy")
    completedBy: Optional[str] = Field(None, alias="completedBy")
    winery: Optional[str] = Field(None, alias="winery")
    fromVessel: Optional[VesselsOut] = Field(None, alias="fromVessel")
    toVessel: Optional[VesselsOut] = Field(None, alias="toVessel")
    lossDetails: Optional[LossDetailsOut] = Field(None, alias="lossDetails")
    additionOps: Optional[AdditionOpsOut] = Field(None, alias="additionOps")
    analysisOps: Optional[AnalysisOpsOut] = Field(None, alias="analysisOps")
    additionalDetails: Optional[str] = Field(None, alias="additionalDetails")
    # last_modified: Optional[str] = Field(None, alias="last_modified")
    
    @field_validator('jobNumber', mode='before')
    def coerce_job_number(cls, v):
        if v is not None:
            return str(v)
        return v

    class Config:
        from_attributes = True
