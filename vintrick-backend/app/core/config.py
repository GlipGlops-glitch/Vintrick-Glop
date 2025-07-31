import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_SERVER: str = os.getenv("DB_SERVER")
    DB_DATABASE: str = os.getenv("DB_DATABASE")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_DRIVER: str = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")
    DB_ENCRYPT: str = os.getenv("DB_ENCRYPT", "yes")
    DB_TRUST_SERVER_CERTIFICATE: str = os.getenv("DB_TRUST_SERVER_CERTIFICATE", "yes")

    @property
    def sqlalchemy_database_url(self) -> str:
        from urllib.parse import quote_plus
        driver = quote_plus(self.DB_DRIVER)
        return (
            f"mssql+pyodbc://{self.DB_USER}:{quote_plus(self.DB_PASSWORD)}@{self.DB_SERVER}/{self.DB_DATABASE}"
            f"?driver={driver}&Encrypt={self.DB_ENCRYPT}&TrustServerCertificate={self.DB_TRUST_SERVER_CERTIFICATE}"
        )

settings = Settings()