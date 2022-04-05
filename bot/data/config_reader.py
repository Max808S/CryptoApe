from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin: int
    etherscan: str
    gas_staion: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config():
    env = Env()
    env.read_env()
    
    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin=env.int("ADMINS"),
            etherscan=env.str("ETHERSCAN_KEY"),
            gas_staion=env.str("ETH_GAS_STATION_KEY")
        )
    )