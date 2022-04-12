import logging

from aiogram import Bot
from data.config_reader import load_config


async def on_startup_notify(bot: Bot) -> None:
    try:
        config = load_config()
        admin = config.tg_bot.admin
        await bot.send_message(admin, "🤖")
        await bot.send_message(admin, f"Привет 👋🏻")
        logging.info(f"ADMIN ID: {admin} are notified about bot launch!")
    except Exception as ex:
        logging.exception(ex)