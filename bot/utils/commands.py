from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    commands = [
            BotCommand(command="btc", description="Получить данные любой монеты по SYMBOL"),
            BotCommand(command="bitcoin", description="Получить данные любой монеты по её названию"),
            BotCommand(command="start", description="Перезапустить бота"),
            BotCommand(command="coins", description="Криптомонеты"),
            BotCommand(command="opensea", description="Показать NFT коллекции"),
            BotCommand(command="trend", description="Топ-7 поиска за 24ч.")
        ]
    await bot.set_my_commands(commands=commands)
