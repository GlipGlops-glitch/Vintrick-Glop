# vintrick-backend/app/models/trans_sum.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base

class VesselDetails(Base):
    __tablename__ = "vessel_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    contentsId = Column(Integer, nullable=True)
    batch = Column(String, nullable=True)
    batchId = Column(Integer, nullable=True)
    volume = Column(Integer, nullable=True)
    volumeUnit = Column(String, nullable=True)
    dip = Column(String, nullable=True)
    state = Column(String, nullable=True)
    rawTaxClass = Column(String, nullable=True)
    federalTaxClass = Column(String, nullable=True)
    stateTaxClass = Column(String, nullable=True)
    program = Column(String, nullable=True)

class Vessel(Base):
    __tablename__ = "vessels"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    vessel_id = Column(Integer, nullable=True)
    # VesselDetails (before/after)
    before_details_id = Column(Integer, ForeignKey("vessel_details.id"), nullable=True)
    after_details_id = Column(Integer, ForeignKey("vessel_details.id"), nullable=True)
    beforeDetails = relationship("VesselDetails", foreign_keys=[before_details_id])
    afterDetails = relationship("VesselDetails", foreign_keys=[after_details_id])
    volOut = Column(Integer, nullable=True)
    volOutUnit = Column(String, nullable=True)
    volIn = Column(Integer, nullable=True)
    volInUnit = Column(String, nullable=True)

class LossDetails(Base):
    __tablename__ = "loss_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    volume = Column(Integer, nullable=True)
    volumeUnit = Column(String, nullable=True)
    reason = Column(String, nullable=True)

class Additives(Base):
    __tablename__ = "additives"
    id = Column(Integer, primary_key=True, autoincrement=True)
    additive_id = Column(Integer, nullable=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)

class AdditionOps(Base):
    __tablename__ = "addition_ops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vesselId = Column(Integer, nullable=True)
    vesselName = Column(String, nullable=True)
    batchId = Column(Integer, nullable=True)
    batchName = Column(String, nullable=True)
    templateId = Column(Integer, nullable=True)
    templateName = Column(String, nullable=True)
    changeToState = Column(String, nullable=True)
    volume = Column(String, nullable=True)
    amount = Column(Float, nullable=True)
    unit = Column(String, nullable=True)
    lotNumbers = Column(String, nullable=True) # Comma separated
    additive_id = Column(Integer, ForeignKey("additives.id"), nullable=True)
    additive = relationship("Additives", foreign_keys=[additive_id])

class MetricAnalysis(Base):
    __tablename__ = "metric_analysis"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    value = Column(Float, nullable=True)
    txtValue = Column(String, nullable=True)
    unit = Column(String, nullable=True)
    analysis_ops_id = Column(Integer, ForeignKey("analysis_ops.id"), nullable=True)

class AnalysisOps(Base):
    __tablename__ = "analysis_ops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vesselId = Column(Integer, nullable=True)
    vesselName = Column(String, nullable=True)
    batchId = Column(Integer, nullable=True)
    batchName = Column(String, nullable=True)
    templateId = Column(Integer, nullable=True)
    templateName = Column(String, nullable=True)
    metrics = relationship("MetricAnalysis", foreign_keys=[MetricAnalysis.analysis_ops_id])

class TransSum(Base):
    __tablename__ = "trans_sums"
    id = Column(Integer, primary_key=True, autoincrement=True)
    formattedDate = Column(String, nullable=True)
    date = Column(Integer, nullable=True)
    operationId = Column(Integer, nullable=True)
    operationTypeId = Column(Integer, nullable=True)
    operationTypeName = Column(String, nullable=True)
    subOperationTypeId = Column(Integer, nullable=True)
    subOperationTypeName = Column(String, nullable=True)
    workorder = Column(String, nullable=True)
    jobNumber = Column(String, nullable=True)
    treatment = Column(String, nullable=True)
    assignedBy = Column(String, nullable=True)
    completedBy = Column(String, nullable=True)
    winery = Column(String, nullable=True)
    from_vessel_id = Column(Integer, ForeignKey("vessels.id"), nullable=True)
    to_vessel_id = Column(Integer, ForeignKey("vessels.id"), nullable=True)
    loss_details_id = Column(Integer, ForeignKey("loss_details.id"), nullable=True)
    addition_ops_id = Column(Integer, ForeignKey("addition_ops.id"), nullable=True)
    analysis_ops_id = Column(Integer, ForeignKey("analysis_ops.id"), nullable=True)
    additionalDetails = Column(String, nullable=True)

    fromVessel = relationship("Vessel", foreign_keys=[from_vessel_id], post_update=True)
    toVessel = relationship("Vessel", foreign_keys=[to_vessel_id], post_update=True)
    lossDetails = relationship("LossDetails", foreign_keys=[loss_details_id])
    additionOps = relationship("AdditionOps", foreign_keys=[addition_ops_id])
    analysisOps = relationship("AnalysisOps", foreign_keys=[analysis_ops_id])