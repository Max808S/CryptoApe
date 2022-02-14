from aiogram import Bot, Dispatcher
from data.config import BOT_TOKEN


# TODO
# storage = MemoryStorage()

# creating bot
bot = Bot(token=BOT_TOKEN, parse_mode="HTML") 
dp = Dispatcher(bot) # storage=storage