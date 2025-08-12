# vintrick-backend/app/crud/trans_sum.py

from sqlalchemy.orm import Session
from app.models.trans_sum import (
    VesselDetails, Vessels, LossDetails,
    Additives, AdditionOps, MetricAnalysis, AnalysisOps, TransSum
)
from app.schemas.trans_sum import TransSumCreate
from typing import Optional, List

def create_trans_sum(db: Session, trans_sum: TransSumCreate) -> TransSum:
    """
    Creates a new TransSum record with all relationships, using a TransSumCreate Pydantic model.
    """
    tx = trans_sum.model_dump()
    # Removed last_modified
    return insert_trans_sum_transaction(db, tx)

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

    # Vessels (handles both from and to vessel)
    def insert_vessel(vessel, is_from=True):
        if not vessel:
            return None
        before_id = insert_vessel_details(vessel.get("beforeDetails"))
        after_id = insert_vessel_details(vessel.get("afterDetails"))
        v = Vessels(
            name=vessel.get("name"),
            before_details_id=before_id,
            after_details_id=after_id,
            vol_out=vessel.get("volOut") if is_from else None,
            vol_out_unit=vessel.get("volOutUnit") if is_from else None,
            vol_in=vessel.get("volIn") if not is_from else None,
            vol_in_unit=vessel.get("volInUnit") if not is_from else None
        )
        db.add(v)
        db.flush()
        return v.id

    from_vessel_id = insert_vessel(tx.get("fromVessel"), is_from=True)
    to_vessel_id = insert_vessel(tx.get("toVessel"), is_from=False)

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
            additive_id=tx["additionOps"]["additive"].get("additive_id"),
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
            lot_numbers=tx["additionOps"].get("lotNumbers"),
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
        for metric in tx["analysisOps"].get("metrics", []):
            m = MetricAnalysis(
                analysis_ops_id=analysis_ops_id,
                name=metric.get("name"),
                value=metric.get("value"),
                txt_value=metric.get("txtValue"),
                unit=metric.get("unit"),
            )
            db.add(m)

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
        # Removed last_modified
    )
    db.add(trans_sum)
    db.commit()
    db.refresh(trans_sum)
    return trans_sum

def get_all_trans_sums(db: Session, skip: int = 0, limit: int = 50):
    # Removed sorting by last_modified
    query = db.query(TransSum).order_by(TransSum.id.desc())
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
    # Removed update of last_modified
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