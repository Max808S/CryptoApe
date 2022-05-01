import logging
from aiogram import Bot
from services import broadcaster


async def on_startup(bot: Bot, admin_ids: list):
    await broadcaster.broadcast(bot, admin_ids, "Привет 🤖 Бот запущен!")
    logging.info(f"ADMINS {admin_ids} are notified about bot launch!")