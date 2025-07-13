from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://postgres:password@localhost:5432/kpa_db"
    
    # Application
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    
    # File Upload
    max_file_size: int = 10485760  
    upload_dir: str = "uploads"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Create settings instance
settings = Settings()

# Ensure upload directory exists
os.makedirs(settings.upload_dir, exist_ok=True) 