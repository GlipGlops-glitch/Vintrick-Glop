# vintrick-backend/app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:Mtbreeze17!@db:5432/vintrick")

settings = Settings()
