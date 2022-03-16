from aiogram import types

from api_requests.coingecko.token_json import dict_from_cg_categories_csv
from api_requests.coingecko.coingecko import get_cg_categories


async def cg_categories(message: types.Message) -> str:
    """
    Get categories
    """
    result_cg_cat = await get_cg_categories(message.text[1:])
    await message.answer(result_cg_cat)