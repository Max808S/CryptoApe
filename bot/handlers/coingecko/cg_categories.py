from aiogram import types

from api_requests.coingecko.token_json import dict_from_cg_categories_csv
from api_requests.coingecko.coingecko import get_cg_categories


async def cg_categories(message: types.Message) -> str:
    """
    Get categories
    """
    for key, value in dict_from_cg_categories_csv.items():
        if value == message.text[1:]:
            result = await get_cg_categories(key)
    await message.answer(result)