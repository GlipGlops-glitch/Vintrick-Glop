# vintrick-backend/app/schemas/trans_sum.py

from pydantic import BaseModel
from typing import Optional, List

class VesselDetailsOut(BaseModel):
    contents_id: Optional[int]
    batch: Optional[str]
    batch_id: Optional[int]
    volume: Optional[float]
    volume_unit: Optional[str]
    dip: Optional[str]
    state: Optional[str]
    raw_tax_class: Optional[str]
    federal_tax_class: Optional[str]
    state_tax_class: Optional[str]
    program: Optional[str]

class FromVesselOut(BaseModel):
    name: Optional[str]
    before_details: Optional[VesselDetailsOut]
    after_details: Optional[VesselDetailsOut]
    vol_out: Optional[float]
    vol_out_unit: Optional[str]

class ToVesselOut(BaseModel):
    name: Optional[str]
    before_details: Optional[VesselDetailsOut]
    after_details: Optional[VesselDetailsOut]
    vol_in: Optional[float]
    vol_in_unit: Optional[str]

class LossDetailsOut(BaseModel):
    volume: Optional[float]
    volume_unit: Optional[str]
    reason: Optional[str]

class AdditivesOut(BaseModel):
    name: Optional[str]
    description: Optional[str]

class AdditionOpsOut(BaseModel):
    vessel_id: Optional[int]
    vessel_name: Optional[str]
    batch_id: Optional[int]
    batch_name: Optional[str]
    template_id: Optional[int]
    template_name: Optional[str]
    change_to_state: Optional[str]
    volume: Optional[str]
    amount: Optional[float]
    unit: Optional[str]
    additive: Optional[AdditivesOut]

class MetricAnalysisOut(BaseModel):
    name: Optional[str]
    value: Optional[float]
    txt_value: Optional[str]
    unit: Optional[str]

class AnalysisOpsOut(BaseModel):
    vessel_id: Optional[int]
    vessel_name: Optional[str]
    batch_id: Optional[int]
    batch_name: Optional[str]
    template_id: Optional[int]
    template_name: Optional[str]
    metrics: Optional[List[MetricAnalysisOut]] = []

class TransSumOut(BaseModel):
    formatted_date: Optional[str]
    date: Optional[int]
    operation_id: int
    operation_type_id: Optional[int]
    operation_type_name: Optional[str]
    sub_operation_type_id: Optional[int]
    sub_operation_type_name: Optional[str]
    workorder: Optional[str]
    job_number: Optional[str]
    treatment: Optional[str]
    assigned_by: Optional[str]
    completed_by: Optional[str]
    winery: Optional[str]
    from_vessel: Optional[FromVesselOut]
    to_vessel: Optional[ToVesselOut]
    loss_details: Optional[LossDetailsOut]
    addition_ops: Optional[AdditionOpsOut]
    analysis_ops: Optional[AnalysisOpsOut]
    additional_details: Optional[str]

    class Config:
        from_attributes = True

# For creation, you can reuse the Out schemas (except for operation_id, which could be optional)
class TransSumCreate(BaseModel):
    formatted_date: Optional[str]
    date: Optional[int]
    operation_type_id: Optional[int]
    operation_type_name: Optional[str]
    sub_operation_type_id: Optional[int]
    sub_operation_type_name: Optional[str]
    workorder: Optional[str]
    job_number: Optional[str]
    treatment: Optional[str]
    assigned_by: Optional[str]
    completed_by: Optional[str]
    winery: Optional[str]
    from_vessel: Optional[FromVesselOut]
    to_vessel: Optional[ToVesselOut]
    loss_details: Optional[LossDetailsOut]
    addition_ops: Optional[AdditionOpsOut]
    analysis_ops: Optional[AnalysisOpsOut]
    additional_details: Optional[str]