import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "mssql+pyodbc://@SMWECSMDEV10/Higgins_Sandbox?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&encrypt=yes&trustservercertificate=yes"
    )

settings = Settings()