from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    # postgres_user: str
    # postgres_password: str
    # postgres_host: str
    # postgres_port: int
    # postgres_db: str
    postgres_url: str

    @property
    def postgres_dsn(self) -> str:
        return self.postgres_url
        # return (
        #     f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
        #     f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        # )

    class Config:
        env_file = ".env"

app_settings = AppSettings()

