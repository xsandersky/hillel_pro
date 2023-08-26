import os

from pydantic import BaseModel
from yaml import Loader, load

class DataBaseConfig(BaseModel):
    host: str
    port: int
    username: str
    password: str
    db_name: str

    def connection_string(self):
        return f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"

class ApplicationConfig(BaseModel):
    read_database: DataBaseConfig
    write_database: DataBaseConfig


def _load_config() -> ApplicationConfig:
    config_path = os.environ.get("CONFIG_PATH", "config.yml")
    with open(config_path, "r") as f:
        config_data = load(f.read(), Loader)
    return ApplicationConfig(**config_data)


config = _load_config()