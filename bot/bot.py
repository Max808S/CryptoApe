import asyncio
import logging

from magic_filter import F
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from handlers import default_commands, admin_commands, coingecko_commands

from utils.commands import set_bot_commands
from utils.notify_admins import on_startup

from config_reader import load_config
from middlewares.throttling import ThrottlingMiddleware
from middlewares.db import DbSessionMiddleware

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


async def main() -> None:
    # Reading config file
    config = load_config(".env")

    # Creating DB engine for PostgreSQL
    engine = create_async_engine(
        config.tg_bot.postgres_dsn, 
        future=True, 
        echo=False
    )
    
    # Creating DB connections pool
    db_pool = sessionmaker(
        engine, 
        expire_on_commit=False, 
        class_=AsyncSession
    )

    # Creating bot
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Add admin filter to admin_router
    admin_commands.admin_router.message.filter(F.chat.id == config.tg_bot.admin_ids)

    # Register routers with handlers
    dp.include_router(default_commands.user_router)
    dp.include_router(admin_commands.admin_router)
    dp.include_router(coingecko_commands.coingecko_router)
    
    # Register middlewares
    dp.message.middleware(ThrottlingMiddleware())
    dp.message.middleware(DbSessionMiddleware(db_pool))

    # Admin notification about bot launch
    await on_startup(bot, config.tg_bot.admin_ids)

    # Register /-commands
    await set_bot_commands(bot)

    try:
        await dp.start_polling(
            bot, 
            allowed_updates=dp.resolve_used_update_types()
        )
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
    finally:
        logging.warning('Goodbye!')