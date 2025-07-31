from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = settings.sqlalchemy_database_url

# Mask password for logging
def mask_password_in_url(url: str) -> str:
    import re
    return re.sub(r':[^:@]+@', ':***@', url)

logger.info(f"Using SQLAlchemy connection string: {mask_password_in_url(DATABASE_URL)}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()