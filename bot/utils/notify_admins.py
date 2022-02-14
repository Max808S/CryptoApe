
from loader import logging, Dispatcher
from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, f'Привет! Я включился :)')
        except Exception as err:
            logging.exception(err)