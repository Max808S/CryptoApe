import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from handlers import default_commands, admin_commands, coingecko_commands

from utils.commands import set_bot_commands
from utils.notify_admins import on_startup_notify

from data.config_reader import load_config
from middlewares.throttling import ThrottlingMiddleware
from magic_filter import F


async def main() -> None:
    # Reading config file
    config = load_config()

    # Creating bot
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Add admin filter to admin_router
    admin_commands.admin_router.message.filter(F.chat.id == config.tg_bot.admin)

    # Register routers with handlers
    dp.include_router(default_commands.user_router)
    dp.include_router(admin_commands.admin_router)
    dp.include_router(coingecko_commands.coingecko_router)
    
    # Register middleware for throttling
    dp.message.middleware(ThrottlingMiddleware())

    # Notification for admins about the start of the bot TODO async def on_startup(dp): 
    await on_startup_notify(bot)
    
    # Register /-commands
    await set_bot_commands(bot)

    try:
        await dp.start_polling(
            bot, 
            allowed_updates=dp.resolve_used_update_types()
        ) # on_startup=on_startup
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
    finally:
        logging.warning('Goodbye!')