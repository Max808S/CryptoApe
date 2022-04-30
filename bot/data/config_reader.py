from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    etherscan: str
    gas_staion: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    
    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            etherscan=env.str("ETHERSCAN_KEY"),
            gas_staion=env.str("ETH_GAS_STATION_KEY")
        )
    )