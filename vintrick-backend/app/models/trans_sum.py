# vintrick-backend/app/models/trans_sum.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from app.core.db import Base

class VesselDetails(Base):
    __tablename__ = "vessel_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    contents_id = Column(Integer, nullable=True)
    batch = Column(String, nullable=True)
    batch_id = Column(Integer, nullable=True)
    volume = Column(Float, nullable=True)
    volume_unit = Column(String, nullable=True)
    dip = Column(String, nullable=True)
    state = Column(String, nullable=True)
    raw_tax_class = Column(String, nullable=True)
    federal_tax_class = Column(String, nullable=True)
    state_tax_class = Column(String, nullable=True)
    program = Column(String, nullable=True)

class FromVessel(Base):
    __tablename__ = "from_vessel"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    before_details_id = Column(Integer, ForeignKey("vessel_details.id"))
    after_details_id = Column(Integer, ForeignKey("vessel_details.id"))
    vol_out = Column(Float, nullable=True)
    vol_out_unit = Column(String, nullable=True)
    before_details = relationship("VesselDetails", foreign_keys=[before_details_id])
    after_details = relationship("VesselDetails", foreign_keys=[after_details_id])

class ToVessel(Base):
    __tablename__ = "to_vessel"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    before_details_id = Column(Integer, ForeignKey("vessel_details.id"))
    after_details_id = Column(Integer, ForeignKey("vessel_details.id"))
    vol_in = Column(Float, nullable=True)
    vol_in_unit = Column(String, nullable=True)
    before_details = relationship("VesselDetails", foreign_keys=[before_details_id])
    after_details = relationship("VesselDetails", foreign_keys=[after_details_id])

class LossDetails(Base):
    __tablename__ = "loss_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    volume = Column(Float, nullable=True)
    volume_unit = Column(String, nullable=True)
    reason = Column(String, nullable=True)

class Additives(Base):
    __tablename__ = "additives"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)

class AdditionOps(Base):
    __tablename__ = "addition_ops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vessel_id = Column(Integer, nullable=True)
    vessel_name = Column(String, nullable=True)
    batch_id = Column(Integer, nullable=True)
    batch_name = Column(String, nullable=True)
    template_id = Column(Integer, nullable=True)
    template_name = Column(String, nullable=True)
    change_to_state = Column(String, nullable=True)
    volume = Column(String, nullable=True)
    amount = Column(Float, nullable=True)
    unit = Column(String, nullable=True)
    additive_id = Column(Integer, ForeignKey("additives.id"))
    additive = relationship("Additives")
    # lotNumbers could be represented as a separate table if needed

class MetricAnalysis(Base):
    __tablename__ = "metric_analysis"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    value = Column(Float, nullable=True)
    txt_value = Column(String, nullable=True)
    unit = Column(String, nullable=True)

class AnalysisOps(Base):
    __tablename__ = "analysis_ops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vessel_id = Column(Integer, nullable=True)
    vessel_name = Column(String, nullable=True)
    batch_id = Column(Integer, nullable=True)
    batch_name = Column(String, nullable=True)
    template_id = Column(Integer, nullable=True)
    template_name = Column(String, nullable=True)
    # One-to-many relationship: metrics
    metrics = relationship("MetricAnalysis")

class TransSum(Base):
    __tablename__ = "trans_sum"
    id = Column(Integer, primary_key=True, autoincrement=True)
    formatted_date = Column(String, nullable=True)
    date = Column(Integer, nullable=True)
    operation_id = Column(Integer, unique=True, nullable=False)
    operation_type_id = Column(Integer, nullable=True)
    operation_type_name = Column(String, nullable=True)
    sub_operation_type_id = Column(Integer, nullable=True)
    sub_operation_type_name = Column(String, nullable=True)
    workorder = Column(String, nullable=True)
    job_number = Column(String, nullable=True)
    treatment = Column(String, nullable=True)
    assigned_by = Column(String, nullable=True)
    completed_by = Column(String, nullable=True)
    winery = Column(String, nullable=True)
    from_vessel_id = Column(Integer, ForeignKey("from_vessel.id"))
    to_vessel_id = Column(Integer, ForeignKey("to_vessel.id"))
    loss_details_id = Column(Integer, ForeignKey("loss_details.id"))
    addition_ops_id = Column(Integer, ForeignKey("addition_ops.id"))
    analysis_ops_id = Column(Integer, ForeignKey("analysis_ops.id"))
    additional_details = Column(String, nullable=True)  # Consider a separate table for key-value pairs

    from_vessel = relationship("FromVessel", foreign_keys=[from_vessel_id])
    to_vessel = relationship("ToVessel", foreign_keys=[to_vessel_id])
    loss_details = relationship("LossDetails", foreign_keys=[loss_details_id])
    addition_ops = relationship("AdditionOps", foreign_keys=[addition_ops_id])
    analysis_ops = relationship("AnalysisOps", foreign_keys=[analysis_ops_id])