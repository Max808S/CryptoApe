from aiogram import types

from api_requests.coingecko.coingecko import get_price
from api_requests.coingecko.trending_coins import get_trending_coins
from api_requests.coingecko.token_json import dict_from_tokens_csv
from data.text_file import trend_text


async def token_name(message: types.Message) -> str:
    """
    Checking the coin in the database (CSV COINS LIST) by name.
    """
    result = await get_price(message.text[1:])
    # await message.delete()
    # await message.delete(message.message_id)
    await message.answer(result)

    
async def token_id(message: types.Message) -> str:
    """
    Checking the coin in the database (CSV COINS LIST) by id.
    """
    for key, value in dict_from_tokens_csv.items():
        if value == message.text[1:]:
            result = await get_price(key)
    await message.answer(result)


async def trend(message: types.Message) -> str:
    """
    Get trending search coins (Top-7) on CoinGecko in the last 24 hours.
    /api/v3/search/trending
    """
    result = await get_trending_coins()
    await message.answer(
        f'{trend_text}\n\n{result}'
    )