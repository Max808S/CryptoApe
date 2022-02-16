from loader import dp
from aiogram import Dispatcher, types

from api_requests.coingecko import get_bitcoin_price


# Хэндлер на команду /price
# @dp.message_handler(commands=["price"])
async def priceb(message: types.Message):
    await message.answer(f"Цена биткоина = {await get_bitcoin_price()}")



def register_coins_commands(dp: Dispatcher):
    dp.register_message_handler(priceb, commands='price')