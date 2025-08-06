from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Blend(Base):
    __tablename__ = "blends"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String(100), nullable=False)
    Brand = Column(String(100), nullable=True)
    Varietal = Column(String(100), nullable=True)
    Vintage = Column(String(20), nullable=True)
    WineType = Column(String(50), nullable=True)