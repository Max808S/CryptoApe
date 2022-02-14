import asyncio
from loader import *

from handlers.default_commands import register_commands
from handlers.opensea.collections import *

from utils.notify_admins import on_startup_notify
# from utils.commands import *  # TODO

# broadcaster TODO
# from services.broadcaster import *


async def main():
    # [1] Logging from loader.py

    # TODO Reading config file
    # config = load_config()

    await on_startup_notify(dp)

    # TODO
    # await set_my_commands(dp)

    # [2] Creating bot and its dispatcher  in [loader.py]

    # Register handlers
    register_commands(dp)
    register_opensea(dp)
    # register_callbacks(dp)
    
    # Register middlewares TODO
    # dp.middleware.setup(DbSessionMiddleware(db_pool))

    # Register /-commands in UI    IDK TODO wtf
    # await set_bot_commands(bot)

    # Starting polling or TODO webhooks 
    try:
        await dp.skip_updates() # use to skip pending updates MAYBE
        await dp.start_polling() # allowed_updates=False
        
    finally:
        await dp._closed()
        # await dp.storage.wait_closed()
        # await bot.session.close()



try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    logging.error("Bot stopped!")