import logging

from aiogram import Bot, Dispatcher

from data.config import BOT_TOKEN


# TODO
# storage = MemoryStorage()

# creating bot
bot = Bot(token=BOT_TOKEN, parse_mode="HTML") 
dp = Dispatcher(bot) # storage=storage


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO) # level=logging.DEBUG

# coin notify 
log = logging.getLogger('broadcast')