# vintrick-backend/app/crud/trans_sum.py

from sqlalchemy.orm import Session
from app.models.trans_sum import (
    VesselDetails, FromVessel, ToVessel, LossDetails,
    Additives, AdditionOps, MetricAnalysis, AnalysisOps, TransSum
)
from app.schemas.trans_sum import TransSumCreate
from typing import Optional, List
from datetime import datetime, timezone

# ----------- FIX: create_trans_sum should call insert_trans_sum_transaction -----------

def create_trans_sum(db: Session, trans_sum: TransSumCreate) -> TransSum:
    """
    Creates a new TransSum record with all relationships, using a TransSumCreate Pydantic model.
    """
    # Convert Pydantic to dict for nested processing
    tx = trans_sum.model_dump()
    # Optionally set last_modified if your model expects it
    tx["last_modified"] = datetime.now(timezone.utc)
    # Use the normalized insert function
    return insert_trans_sum_transaction(db, tx)

# ----------- Existing normalized insert function -----------

def insert_trans_sum_transaction(db: Session, tx: dict):
    # Vessel Details helpers
    def insert_vessel_details(d):
        if not d: return None
        vd = VesselDetails(
            contents_id=d.get("contentsId"),
            batch=d.get("batch"),
            batch_id=d.get("batchId"),
            volume=d.get("volume"),
            volume_unit=d.get("volumeUnit"),
            dip=d.get("dip"),
            state=d.get("state"),
            raw_tax_class=d.get("rawTaxClass"),
            federal_tax_class=d.get("federalTaxClass"),
            state_tax_class=d.get("stateTaxClass"),
            program=d.get("program"),
        )
        db.add(vd)
        db.flush()
        return vd.id

    # FromVessel
    from_vessel_id = None
    if tx.get("fromVessel"):
        before_id = insert_vessel_details(tx["fromVessel"].get("beforeDetails"))
        after_id = insert_vessel_details(tx["fromVessel"].get("afterDetails"))
        fv = FromVessel(
            name=tx["fromVessel"].get("name"),
            before_details_id=before_id,
            after_details_id=after_id,
            vol_out=tx["fromVessel"].get("volOut"),
            vol_out_unit=tx["fromVessel"].get("volOutUnit"),
        )
        db.add(fv)
        db.flush()
        from_vessel_id = fv.id

    # ToVessel
    to_vessel_id = None
    if tx.get("toVessel"):
        before_id = insert_vessel_details(tx["toVessel"].get("beforeDetails"))
        after_id = insert_vessel_details(tx["toVessel"].get("afterDetails"))
        tv = ToVessel(
            name=tx["toVessel"].get("name"),
            before_details_id=before_id,
            after_details_id=after_id,
            vol_in=tx["toVessel"].get("volIn"),
            vol_in_unit=tx["toVessel"].get("volInUnit"),
        )
        db.add(tv)
        db.flush()
        to_vessel_id = tv.id

    # LossDetails
    loss_details_id = None
    if tx.get("lossDetails"):
        ld = LossDetails(
            volume=tx["lossDetails"].get("volume"),
            volume_unit=tx["lossDetails"].get("volumeUnit"),
            reason=tx["lossDetails"].get("reason"),
        )
        db.add(ld)
        db.flush()
        loss_details_id = ld.id

    # Additives
    additive_id = None
    if tx.get("additionOps") and tx["additionOps"].get("additive"):
        ad = Additives(
            name=tx["additionOps"]["additive"].get("name"),
            description=tx["additionOps"]["additive"].get("description"),
        )
        db.add(ad)
        db.flush()
        additive_id = ad.id

    # AdditionOps
    addition_ops_id = None
    if tx.get("additionOps"):
        ao = AdditionOps(
            vessel_id=tx["additionOps"].get("vesselId"),
            vessel_name=tx["additionOps"].get("vesselName"),
            batch_id=tx["additionOps"].get("batchId"),
            batch_name=tx["additionOps"].get("batchName"),
            template_id=tx["additionOps"].get("templateId"),
            template_name=tx["additionOps"].get("templateName"),
            change_to_state=tx["additionOps"].get("changeToState"),
            volume=tx["additionOps"].get("volume"),
            amount=tx["additionOps"].get("amount"),
            unit=tx["additionOps"].get("unit"),
            additive_id=additive_id,
        )
        db.add(ao)
        db.flush()
        addition_ops_id = ao.id

    # AnalysisOps & MetricAnalysis
    analysis_ops_id = None
    if tx.get("analysisOps"):
        ao = AnalysisOps(
            vessel_id=tx["analysisOps"].get("vesselId"),
            vessel_name=tx["analysisOps"].get("vesselName"),
            batch_id=tx["analysisOps"].get("batchId"),
            batch_name=tx["analysisOps"].get("batchName"),
            template_id=tx["analysisOps"].get("templateId"),
            template_name=tx["analysisOps"].get("templateName"),
        )
        db.add(ao)
        db.flush()
        analysis_ops_id = ao.id
        # Insert each metric
        for metric in tx["analysisOps"].get("metrics", []):
            m = MetricAnalysis(
                analysis_ops_id=analysis_ops_id,
                name=metric.get("name"),
                value=metric.get("value"),
                txt_value=metric.get("txtValue"),
                unit=metric.get("unit"),
            )
            db.add(m)

    # TransSum
    trans_sum = TransSum(
        formatted_date=tx.get("formattedDate"),
        date=tx.get("date"),
        operation_id=tx.get("operationId"),
        operation_type_id=tx.get("operationTypeId"),
        operation_type_name=tx.get("operationTypeName"),
        sub_operation_type_id=tx.get("subOperationTypeId"),
        sub_operation_type_name=tx.get("subOperationTypeName"),
        workorder=tx.get("workorder"),
        job_number=tx.get("jobNumber"),
        treatment=tx.get("treatment"),
        assigned_by=tx.get("assignedBy"),
        completed_by=tx.get("completedBy"),
        winery=tx.get("winery"),
        from_vessel_id=from_vessel_id,
        to_vessel_id=to_vessel_id,
        loss_details_id=loss_details_id,
        addition_ops_id=addition_ops_id,
        analysis_ops_id=analysis_ops_id,
        additional_details=tx.get("additionalDetails"),
        last_modified=tx.get("last_modified", datetime.now(timezone.utc)),
    )
    db.add(trans_sum)
    db.commit()
    db.refresh(trans_sum)
    return trans_sum

# ----------- Query/Update/Delete functions -----------

def get_all_trans_sums(db: Session, skip: int = 0, limit: int = 50):
    query = db.query(TransSum).order_by(TransSum.last_modified.desc(), TransSum.id.desc())
    total = query.count()
    if skip:
        query = query.offset(skip)
    if limit:
        query = query.limit(limit)
    return query.all(), total

def get_trans_sum_by_uid(db: Session, uid: str) -> Optional[TransSum]:
    return db.query(TransSum).filter(TransSum.id == uid).first()

def update_trans_sum(db: Session, uid: str, updates: TransSumCreate) -> Optional[TransSum]:
    db_obj = get_trans_sum_by_uid(db, uid)
    if db_obj is None:
        return None
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db_obj.last_modified = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_trans_sum(db: Session, uid: str) -> bool:
    db_obj = get_trans_sum_by_uid(db, uid)
    if db_obj:
        db.delete(db_obj)
        db.commit()
        return True
    return False