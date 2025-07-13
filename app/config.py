# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    debug: bool
    host: str
    port: int
    max_file_size: int
    upload_dir: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
