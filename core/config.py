from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

class AppSettings(BaseSettings):
    postgres_dsn: PostgresDsn

    class Config:
        env_file = ".env"

app_settings = AppSettings()

