# vintrick-backend/app/models/trans_sum.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, BigInteger
from sqlalchemy.orm import relationship
from app.core.db import Base

# VesselDetails table
class VesselDetails(Base):
    __tablename__ = "vessel_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    contents_id = Column(Integer, nullable=True, name="contentsId")
    batch = Column(String(255), nullable=True, name="batch")
    batch_id = Column(Integer, nullable=True, name="batchId")
    volume = Column(Integer, nullable=True, name="volume")
    volume_unit = Column(String(32), nullable=True, name="volumeUnit")
    dip = Column(String(32), nullable=True, name="dip")
    state = Column(String(64), nullable=True, name="state")
    raw_tax_class = Column(String(128), nullable=True, name="rawTaxClass")
    federal_tax_class = Column(String(128), nullable=True, name="federalTaxClass")
    state_tax_class = Column(String(128), nullable=True, name="stateTaxClass")
    program = Column(String(128), nullable=True, name="program")

# Vessels table (used for both FromVessel and ToVessel)
class Vessels(Base):
    __tablename__ = "vessels"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True, name="name")
    vessel_id = Column(Integer, nullable=True, name="vessel_id")
    before_details_id = Column(Integer, ForeignKey("vessel_details.id"), nullable=True, name="before_details_id")
    after_details_id = Column(Integer, ForeignKey("vessel_details.id"), nullable=True, name="after_details_id")
    vol_out = Column(Integer, nullable=True, name="volOut")
    vol_out_unit = Column(String(32), nullable=True, name="volOutUnit")
    vol_in = Column(Integer, nullable=True, name="volIn")
    vol_in_unit = Column(String(32), nullable=True, name="volInUnit")
    before_details = relationship("VesselDetails", foreign_keys=[before_details_id])
    after_details = relationship("VesselDetails", foreign_keys=[after_details_id])

# LossDetails table
class LossDetails(Base):
    __tablename__ = "loss_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    volume = Column(Integer, nullable=True, name="volume")
    volume_unit = Column(String(32), nullable=True, name="volumeUnit")
    reason = Column(String(255), nullable=True, name="reason")

# Additives table
class Additives(Base):
    __tablename__ = "additives"
    id = Column(Integer, primary_key=True, autoincrement=True)
    additive_id = Column(Integer, nullable=True, name="additive_id")
    name = Column(String(255), nullable=True, name="name")
    description = Column(String(255), nullable=True, name="description")

# AdditionOps table
class AdditionOps(Base):
    __tablename__ = "addition_ops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vessel_id = Column(Integer, nullable=True, name="vesselId")
    vessel_name = Column(String(255), nullable=True, name="vesselName")
    batch_id = Column(Integer, nullable=True, name="batchId")
    batch_name = Column(String(255), nullable=True, name="batchName")
    template_id = Column(Integer, nullable=True, name="templateId")
    template_name = Column(String(255), nullable=True, name="templateName")
    change_to_state = Column(String(255), nullable=True, name="changeToState")
    volume = Column(String(64), nullable=True, name="volume")
    amount = Column(Float, nullable=True, name="amount")
    unit = Column(String(32), nullable=True, name="unit")
    lot_numbers = Column(String, nullable=True, name="lotNumbers")
    additive_id = Column(Integer, ForeignKey("additives.id"), nullable=True, name="additive_id")
    additive = relationship("Additives", foreign_keys=[additive_id])

# AnalysisOps table
class AnalysisOps(Base):
    __tablename__ = "analysis_ops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vessel_id = Column(Integer, nullable=True, name="vesselId")
    vessel_name = Column(String(255), nullable=True, name="vesselName")
    batch_id = Column(Integer, nullable=True, name="batchId")
    batch_name = Column(String(255), nullable=True, name="batchName")
    template_id = Column(Integer, nullable=True, name="templateId")
    template_name = Column(String(255), nullable=True, name="templateName")
    metrics = relationship("MetricAnalysis", back_populates="analysis_ops", cascade="all, delete-orphan")

# MetricAnalysis table
class MetricAnalysis(Base):
    __tablename__ = "metric_analysis"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True, name="name")
    value = Column(Float, nullable=True, name="value")
    txt_value = Column(String(255), nullable=True, name="txtValue")
    unit = Column(String(32), nullable=True, name="unit")
    analysis_ops_id = Column(Integer, ForeignKey("analysis_ops.id"), nullable=True, name="analysis_ops_id")
    analysis_ops = relationship("AnalysisOps", back_populates="metrics")

# TransSum table
class TransSum(Base):
    __tablename__ = "trans_sums"
    id = Column(Integer, primary_key=True, autoincrement=True)
    formatted_date = Column(String(32), nullable=True, name="formattedDate")
    date = Column(BigInteger, nullable=True, name="date")
    operation_id = Column(Integer, nullable=True, name="operationId")
    operation_type_id = Column(Integer, nullable=True, name="operationTypeId")
    operation_type_name = Column(String(128), nullable=True, name="operationTypeName")
    sub_operation_type_id = Column(Integer, nullable=True, name="subOperationTypeId")
    sub_operation_type_name = Column(String(128), nullable=True, name="subOperationTypeName")
    workorder = Column(String(128), nullable=True, name="workorder")
    job_number = Column(String(128), nullable=True, name="jobNumber")
    treatment = Column(String(128), nullable=True, name="treatment")
    assigned_by = Column(String(128), nullable=True, name="assignedBy")
    completed_by = Column(String(128), nullable=True, name="completedBy")
    winery = Column(String(128), nullable=True, name="winery")
    from_vessel_id = Column(Integer, ForeignKey("vessels.id"), nullable=True, name="from_vessel_id")
    to_vessel_id = Column(Integer, ForeignKey("vessels.id"), nullable=True, name="to_vessel_id")
    loss_details_id = Column(Integer, ForeignKey("loss_details.id"), nullable=True, name="loss_details_id")
    addition_ops_id = Column(Integer, ForeignKey("addition_ops.id"), nullable=True, name="addition_ops_id")
    analysis_ops_id = Column(Integer, ForeignKey("analysis_ops.id"), nullable=True, name="analysis_ops_id")
    additional_details = Column(String, nullable=True, name="additionalDetails")
    # last_modified = Column(DateTime, nullable=True, name="last_modified")

    from_vessel = relationship("Vessels", foreign_keys=[from_vessel_id])
    to_vessel = relationship("Vessels", foreign_keys=[to_vessel_id])
    loss_details = relationship("LossDetails", foreign_keys=[loss_details_id])
    addition_ops = relationship("AdditionOps", foreign_keys=[addition_ops_id])
    analysis_ops = relationship("AnalysisOps", foreign_keys=[analysis_ops_id])