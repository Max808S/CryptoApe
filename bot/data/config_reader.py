from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin: int

@dataclass
class Config:
    tg_bot: TgBot


def load_config():
    env = Env()
    env.read_env()
    
    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin=env.int("ADMINS") 
        )
    )