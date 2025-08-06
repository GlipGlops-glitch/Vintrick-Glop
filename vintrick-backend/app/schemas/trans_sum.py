# vintrick-backend/app/schemas/trans_sum.py

from pydantic import BaseModel
from typing import Optional, List

class VesselDetails(BaseModel):
    contentsId: Optional[int]
    batch: Optional[str]
    batchId: Optional[int]
    volume: Optional[int]
    volumeUnit: Optional[str]
    dip: Optional[str]
    state: Optional[str]
    rawTaxClass: Optional[str]
    federalTaxClass: Optional[str]
    stateTaxClass: Optional[str]
    program: Optional[str]

class Vessel(BaseModel):
    name: Optional[str]
    id: Optional[int]
    beforeDetails: Optional[VesselDetails]
    afterDetails: Optional[VesselDetails]
    volOut: Optional[int]
    volOutUnit: Optional[str]
    volIn: Optional[int]
    volInUnit: Optional[str]

class LossDetails(BaseModel):
    volume: Optional[int]
    volumeUnit: Optional[str]
    reason: Optional[str]

class Additives(BaseModel):
    id: Optional[int]
    additive_id: Optional[int]
    name: Optional[str]
    description: Optional[str]

class AdditionOps(BaseModel):
    vesselId: Optional[int]
    vesselName: Optional[str]
    batchId: Optional[int]
    batchName: Optional[str]
    templateId: Optional[int]
    templateName: Optional[str]
    changeToState: Optional[str]
    volume: Optional[str]
    amount: Optional[float]
    unit: Optional[str]
    lotNumbers: Optional[List[str]]
    additive: Optional[Additives]

class MetricAnalysis(BaseModel):
    id: Optional[int]
    name: Optional[str]
    value: Optional[float]
    txtValue: Optional[str]
    unit: Optional[str]

class AnalysisOps(BaseModel):
    vesselId: Optional[int]
    vesselName: Optional[str]
    batchId: Optional[int]
    batchName: Optional[str]
    templateId: Optional[int]
    templateName: Optional[str]
    metrics: Optional[List[MetricAnalysis]]

class TransSumBase(BaseModel):
    formattedDate: Optional[str]
    date: Optional[int]
    operationId: Optional[int]
    operationTypeId: Optional[int]
    operationTypeName: Optional[str]
    subOperationTypeId: Optional[int]
    subOperationTypeName: Optional[str]
    workorder: Optional[str]
    jobNumber: Optional[str]
    treatment: Optional[str]
    assignedBy: Optional[str]
    completedBy: Optional[str]
    winery: Optional[str]
    fromVessel: Optional[Vessel]
    toVessel: Optional[Vessel]
    lossDetails: Optional[LossDetails]
    additionOps: Optional[AdditionOps]
    analysisOps: Optional[AnalysisOps]
    additionalDetails: Optional[str]

class TransSumCreate(TransSumBase):
    pass

class TransSumOut(TransSumBase):
    id: int

    class Config:
        from_attributes = True

class TransSumResponse(BaseModel):
    status: str
    message: Optional[str]
    transactionSummaries: List[TransSumOut]