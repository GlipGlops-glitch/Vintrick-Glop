# vintrick-backend/app/api/routes/harvestloads.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas import HarvestLoad
from app.crud import harvestload
from app.api.deps import get_db

router = APIRouter()

@router.get("/harvestloads/", response_model=dict)
def list_harvestloads(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, gt=0),
    db: Session = Depends(get_db)
):
    items, total = harvestload.get_all_harvestloads(db, skip=skip, limit=limit)
    return {"items": items, "total": total}

@router.get("/harvestloads/{load_id}", response_model=HarvestLoad)
def read_harvestload(load_id: str, db: Session = Depends(get_db)):
    db_load = harvestload.get_harvestload_by_uid(db, load_id)
    if db_load is None:
        raise HTTPException(status_code=404, detail="HarvestLoad not found")
    return db_load

@router.patch("/harvestloads/{load_id}", response_model=HarvestLoad)
def update_harvestload(
    load_id: str, updated_load: HarvestLoadCreate, db: Session = Depends(get_db)
):
    db_obj = harvestload.update_harvestload(db, load_id, updated_load)
    if not db_obj:
        raise HTTPException(status_code=404, detail="HarvestLoad not found")
    return db_obj

@router.post("/harvestloads/", response_model=HarvestLoad)
def create_harvestload(
    load: HarvestLoadCreate, db: Session = Depends(get_db)
):
    try:
        return harvestload.create_harvestload(db, load)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/harvestloads/{load_id}")
def delete_harvestload(load_id: str, db: Session = Depends(get_db)):
    deleted = harvestload.delete_harvestload(db, load_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="HarvestLoad not found")
    return {"ok": True}

















# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.schemas import HarvestLoadCreate, HarvestLoad
# from app.services import harvest_load_service
# from app.api.deps import get_db

# router = APIRouter()


# @router.post("/harvestloads/", response_model=HarvestLoad)
# def create_harvestload(
#     load: HarvestLoadCreate, db: Session = Depends(get_db)
# ):
#     try:
#         return harvest_load_service.create_harvestload(db, load)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @router.get("/harvestloads/{load_id}", response_model=HarvestLoad)
# def read_harvestload(load_id: str, db: Session = Depends(get_db)):
#     db_load = harvest_load_service.get_harvestload(db, load_id)
#     if db_load is None:
#         raise HTTPException(status_code=404, detail="HarvestLoad not found")
#     return db_load


# @router.get("/harvestloads/", response_model=list[HarvestLoad])
# def list_harvestloads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return harvest_load_service.get_all_harvestloads(db)


# @router.put("/harvestloads/{load_id}", response_model=HarvestLoad)
# def update_harvestload(
#     load_id: str, updated_load: HarvestLoadCreate, db: Session = Depends(get_db)
# ):
#     try:
#         return harvest_load_service.update_harvestload(db, load_id, updated_load)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.patch("/harvestloads/{load_id}", response_model=HarvestLoad)
# def update_harvestload(
#     load_id: str, updated_load: HarvestLoadCreate, db: Session = Depends(get_db)
# ):
#     try:
#         return harvest_load_service.update_harvestload(db, load_id, updated_load)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @router.delete("/harvestloads/{load_id}")
# def delete_harvestload(load_id: str, db: Session = Depends(get_db)):
#     try:
#         harvest_load_service.delete_harvestload(db, load_id)
#         return {"ok": True}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
