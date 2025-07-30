import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "mssql+pyodbc://harvest_user:h@rvest_smwe123!@SMWECSMDEV10/Higgins_Sandbox?driver=ODBC+Driver+18+for+SQL+Server"
    )

settings = Settings()