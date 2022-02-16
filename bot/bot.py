import asyncio
from loader import dp, bot

from handlers.default_commands import register_commands
from handlers.coingecko.coins import register_coins_commands
from handlers.opensea.collections import register_opensea

from utils.misc.logging import logging
from utils.notify_admins import on_startup_notify
from utils.commands import set_bot_commands


# broadcaster TODO
# from services.broadcaster import *


async def main() -> None:
    # Reading config file TODO
    # config = load_config()

    # bot start admins notify
    await on_startup_notify(dp)

    # Register handlers
    register_coins_commands(dp)
    register_opensea(dp)
    register_commands(dp)    # START / HELP
    # register_callbacks(dp)

    # Register middlewares TODO
    # dp.middleware.setup(DbSessionMiddleware(db_pool))

    # Register /-commands
    await set_bot_commands(bot)

    # Starting polling or TODO webhooks 
    try:
        await dp.skip_updates() # use to skip pending updates TODO
        await dp.start_polling() # allowed_updates=False
        
    finally:
        # await dp._closed()
        # await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
    finally:
        logging.warning('Goodye!')