from typing import Literal, Optional

from pydantic import BaseSettings
from yarl import URL

from reworkd_platform.constants import ENV_PREFIX


LOG_LEVEL = Literal[
    "NOTSET",
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "FATAL",
]

ENVIRONMENT = Literal[
    "development",
    "production",
]


class Settings(BaseSettings):
    """
    Application settings.
    """

    # Application settings
    host: str = "127.0.0.1"
    port: int = 8000
    workers_count: int = 1
    reload: bool = True
    environment: ENVIRONMENT = "development"
    log_level: LOG_LEVEL = "INFO"

    # Security settings
    secret_signing_key: str = "JF52S66x6WMoifP5gZreiguYs9LYMn0lkXqgPYoNMD0="

    # Frontend URL for CORS
    frontend_url: str = "http://localhost:3000"
    allowed_origins_regex: Optional[str] = None

    # Variables for the database
    db_host: str = "localhost"
    db_port: int = 3308
    db_user: str = "reworkd_platform"
    db_pass: str = "reworkd_platform"
    db_base: str = "reworkd_platform"
    db_echo: bool = False
    db_ca_path: Optional[str] = None

    # Sentry's configuration.
    sentry_dsn: Optional[str] = None
    sentry_sample_rate: float = 1.0

    # Application Settings
    ff_mock_mode_enabled: bool = False  # Controls whether calls are mocked
    max_loops: int = 25  # Maximum number of loops to run

    @property
    def db_url(self) -> URL:
        return URL.build(
            scheme="mysql+aiomysql",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}",
        )

    class Config:
        env_file = ".env"
        env_prefix = ENV_PREFIX
        env_file_encoding = "utf-8"


settings = Settings()
