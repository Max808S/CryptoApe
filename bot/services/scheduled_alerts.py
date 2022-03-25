import asyncio
import logging

from aiogram import Bot

from data.config_reader import load_config
config = load_config()


async def scheduled_task(bot: Bot) -> None:
    emoji = "💸"
    while True:
        await bot.send_message(config.tg_bot.admin, emoji)
        await asyncio.sleep(10.0)
        logging.info(f"Message {emoji} send to user ID: {config.tg_bot.admin}")

# asyncio.create_task(scheduled_task(bot))