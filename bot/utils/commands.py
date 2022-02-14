from loader import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    commands = [
            BotCommand(command="start" or "restart", description="Перезапустить бота"),
            BotCommand(command="opensea", description="Показать NFT коллекции")
        ]
    await bot.set_my_commands(commands=commands)