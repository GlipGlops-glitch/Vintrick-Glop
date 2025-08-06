# vintrick-backend/app/crud/blend.py

from sqlalchemy.orm import Session
from app.models.blend import Blend
from app.schemas.blend import BlendCreate
from typing import Optional, List

def create_blend(db: Session, blend: BlendCreate) -> Blend:
    data = blend.model_dump()
    db_obj = Blend(**data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_all_blends(db: Session, skip: int = 0, limit: int = 50):
    query = db.query(Blend).order_by(Blend.ID.desc())
    total = query.count()
    if skip:
        query = query.offset(skip)
    if limit:
        query = query.limit(limit)
    return query.all(), total

def get_blend_by_id(db: Session, blend_id: int) -> Optional[Blend]:
    return db.query(Blend).filter(Blend.ID == blend_id).first()

def update_blend(db: Session, blend_id: int, updates: BlendCreate) -> Optional[Blend]:
    db_obj = get_blend_by_id(db, blend_id)
    if db_obj is None:
        return None
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_blend(db: Session, blend_id: int) -> bool:
    db_obj = get_blend_by_id(db, blend_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
        return True
    return False