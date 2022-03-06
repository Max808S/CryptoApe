import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
# from aiogram.dispatcher.fsm.storage.redis import RedisStorage    # TODO

from handlers.default_commands import register_commands
# from handlers.coingecko.coins import register_coins_commands
from handlers.opensea.collections import register_opensea    # TODO

from utils.misc.logging import logging
# from utils.notify_admins import on_startup_notify
from utils.commands import set_bot_commands

# from middlewares.throttling import ThrottlingMiddleware  # TODO
from data.config import BOT_TOKEN

# # broadcaster TODO
# from services.broadcaster import *


async def main() -> None:
    logging.basicConfig(level=logging.WARNING)

    # Reading config file   TODO
    # config = load_config()

    # Creating bot
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML") 

    # Creating Router
    default_router = Router()

    # bot start admins notify   TODO
    # await on_startup_notify(dp)

    # Register handlers
    register_opensea(default_router)  # TODO
    # register_coins_commands(default_router)
    register_commands(default_router)    # START / HELP

    # Создание диспетчера и навешивание роутера     TODO
    # if config.bot.fsm_type == "redis":
    #     storage = RedisStorage.from_url(
    #         url=f"redis://default:{config.redis.password}@{config.redis.host}:{config.redis.port}",
    #         connection_kwargs={"decode_responses": True, "db": config.redis.db}
    #     )
    # else:
    #     storage = MemoryStorage()

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)
    dp.include_router(default_router)

    # Register middlewares TODO
    # dp.message.middleware(ThrottlingMiddleware()) 

    # Register /-commands
    await set_bot_commands(bot)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
    finally:
        logging.warning('Goodye!')