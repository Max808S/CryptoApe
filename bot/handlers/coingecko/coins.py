from aiogram import types

from api_requests.coingecko.trending_coins import get_trending_coins
from api_requests.coingecko.coingecko import get_price
from api_requests.coingecko.token_json import dict_from_csv


async def trend(message: types.Message):
    """
    Get trending search coins (Top-7) on CoinGecko in the last 24 hours.
    /api/v3/search/trending
    """
    await message.answer(
        f"Топ-7 самых популярных монет на CoinGecko "
        f"по поиску пользователей за последние 24 часа "
        f"(в порядке убывания популярности):" 
        f"\n\n{await get_trending_coins()}")
    

async def token_id(message: types.Message) -> str:
    """
    Checking the coin in the database (CSV COINS LIST) by id.
    """
    result = await get_price(message.text[1:])
    await message.answer(result)

    
async def token_name(message: types.Message) -> str:
    """
    Checking the coin in the database (CSV COINS LIST) by name.
    """
    for key, value in dict_from_csv.items():
        if value == message.text[1:]:
            result = await get_price(key)
    await message.answer(result)



# Хэндлер на команду /price     # TODO
# @dp.message_handler(commands=["price"])
# async def price_btc(message: types.Message):
#     await message.answer(f"Цена биткоина = {await get_bitcoin_price()}")

# async def price_eth(message: types.Message):
#     await message.answer(f"Цена ефириум = {await get_ethereum_price()}")

# def register_coins_commands(router: Router):
    # router.message.register(price_btc, commands='btc')
    # router.message.register(price_eth, commands='eth')
    # router.message.register(trend, commands='trend')
    # router.message.register(token_price, commands='price')
    # router.message.register(same_def_1, commands=csv_keys)
    # router.message.register(same_def_2, commands=csv_values)