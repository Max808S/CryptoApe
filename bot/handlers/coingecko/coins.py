from aiogram import Router, types

from api_requests.coingecko.coingecko import get_bitcoin_price, get_ethereum_price
from api_requests.coingecko.trending_coins import get_trending_coins
# from api_requests.coingecko.coingecko import get_coin_price


# /api/v3/search/trending
# Get trending search coins (Top-7) on CoinGecko in the last 24 hours
async def trend(message: types.Message):
    await message.answer(f"Топ-7 самых популярных монет на CoinGecko "
        f"по поиску пользователей за последние 24 часа (в порядке убывания "
        f"популярности): \n\n{await get_trending_coins()}")


# Хэндлер на команду /price
# @dp.message_handler(commands=["price"])
async def price_btc(message: types.Message):
    await message.answer(f"Цена биткоина = {await get_bitcoin_price()}")


async def price_eth(message: types.Message):
    await message.answer(f"Цена ефириум = {await get_ethereum_price()}")


## TODO
# async def handle_coins(message: types.Message):
#     price = await get_coin_price("eth")
    


def register_coins_commands(router: Router):
    router.message.register(price_btc, commands='btc')
    router.message.register(price_eth, commands='eth')
    router.message.register(trend, commands='trend')

# def register_coins_commands(dp: Dispatcher):
#     dp.register_message_handler(price_btc, commands='btc')
#     dp.register_message_handler(price_eth, commands='eth')
#     dp.register_message_handler(trend, commands='trend')

    # dp.register_message_handler(price_btc, commands='price_btc')
    # dp.register_message_handler(price_eth, commands='price_eth')
