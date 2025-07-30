import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Only read from environment, no hardcoded fallback!
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()