from dataclasses import dataclass
import configparser

@dataclass
class _Config:
    tg_token: str
    db_url: str
    secret_key: str

_config = configparser.ConfigParser()
_config.read("config.cfg")

config = _Config(
    **_config["Config"]
    )