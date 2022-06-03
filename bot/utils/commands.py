from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    commands = [
            BotCommand(command="btc", description="Получить цену любой монеты по тикеру"),
            BotCommand(command="bitcoin", description="Получить цену любой монеты по имени"),
            BotCommand(command="coins", description="Криптовалюты"),
            BotCommand(command="categories", description="Категории"),
            BotCommand(command="ranking", description="Топ-100 по рыночной капитализации"),
            BotCommand(command="trend", description="Топ-7 поиска за 24ч."),
            BotCommand(command="gas", description="Получить текущую цену gwei"),
            BotCommand(command="help", description="Меню навигации"),
            BotCommand(command="start", description="Перезапустить бота")
        ]
    await bot.set_my_commands(commands=commands)