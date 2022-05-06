from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery

from misc.logging import logger
from api_requests.coingecko import get_categories_list, get_categories_list_data
from api_requests.gas_gwei import gas_tracker

from sqlalchemy.ext.asyncio import AsyncSession
from db.requests import add_user
from random import choice

from misc.text_file import (
    help_text, coins_text, disclaimer, main_text,
    category_text, market_cap_category_text, market_cap_change_24h_category_text
)

from keyboards.inline import (
    get_main_keyboard as main_kb,
    get_categories_inline_keyboard as cat_kb,
    get_full_categories_inline_keyboard as full_cat,
    get_back_main_menu_keyboards as bmm_kb,
    get_main_coins_keyboard as mc_kb
)


flags = {"throttling_key": "default"}
user_router = Router(name=__name__)


# MAIN BOT COMMANDS:
@user_router.message(commands={"start", "restart"}, flags=flags)
async def cmd_start(message: types.Message, session: AsyncSession) -> str:
    """
    Get start menu
    Usage: /start command
    """
    start_sticker = "CAACAgIAAxkBAAEO47NiOinvXVKHDyUd9W2lVS9186mXigACVAADQbVWDGq3-McIjQH6IwQ"
    start_text = (
        f'<b>{message.from_user.first_name}, добро пожаловать в CryptoApe сообщество!</b>\n\n'
        f'{disclaimer}'
    )
    await add_user(
        session, 
        message.from_user.id, 
        message.from_user.username,
        message.from_user.full_name
    )
    await message.answer_sticker(sticker=start_sticker)
    await message.answer(
        start_text, 
        disable_web_page_preview=True, 
        reply_markup=main_kb()
    )
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} press 'START' menu"
    )


@user_router.message(commands="help", flags=flags)
async def cmd_help(message: Message) -> str:
    """
    Get help menu
    Usage: /help command
    """
    await message.delete()
    await message.answer("🤖")
    await message.answer(help_text, reply_markup=bmm_kb(), disable_web_page_preview=True)
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} getting 'HELP' menu"
    )


# COINS:
@user_router.message(commands="coins")
async def cmd_coins(message: Message) -> str:
    """
    Get coins menu
    Usage: /coins command
    """
    await message.delete()
    await message.answer("💎")
    await message.answer(coins_text, reply_markup=mc_kb())
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} getting 'COINS' menu"
    )


@user_router.callback_query(F.data == "coins")
async def inline_coins_button(query: CallbackQuery) -> str:
    """
    Get coins menu with inline button
    Usage: press [Coins] button
    """
    await query.message.edit_text(coins_text, reply_markup=mc_kb())
    logger.info(
        f"USER: {query.from_user.full_name} USERNAME: {query.from_user.username} "
        f"ID: {query.from_user.id} getting 'COINS' inline menu"
    )


# CATEGORIES:
@user_router.message(commands="categories")
async def cmd_categories(message: Message) -> str:
    """
    Get category menu
    Usage: /categories command
    """
    await message.delete()
    await message.answer("📂")
    await message.answer(category_text, reply_markup=cat_kb())
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} getting 'CATEGORIES' menu"
    )


@user_router.callback_query(F.data == "categories")
async def inline_categories_button(query: CallbackQuery) -> str:
    """
    Get category menu with inline button
    Usage: press [Categories] button
    """
    await query.message.edit_text(category_text, reply_markup=cat_kb())
    logger.info(
        f"USER: {query.from_user.full_name} USERNAME: {query.from_user.username} "
        f"ID: {query.from_user.id} getting 'CATEGORIES' inline menu"
    )


@user_router.callback_query(F.data == "full_categories")
async def inline_full_categories_button(query: CallbackQuery) -> str:
    """
    List all categories
    """
    result = await get_categories_list()
    await query.message.edit_text(result, reply_markup=full_cat())
    logger.info(
        f"USER: {query.from_user.full_name} USERNAME: {query.from_user.username} "
        f"ID: {query.from_user.id} getting 'ALL CATEGORIES' inline menu"
    )


@user_router.callback_query(F.data == "category_market_cap_desc")
async def inline_categories_market_cap_button(query: CallbackQuery) -> str:
    """
    List all categories sorted by market cap
    """
    result = await get_categories_list_data("market_cap_desc")
    await query.message.edit_text(f"{market_cap_category_text}\n\n{result}", reply_markup=cat_kb())
    logger.info(
        f"USER: {query.from_user.full_name} USERNAME: {query.from_user.username} "
        f"ID: {query.from_user.id} getting 'CATEGORIES by market cap' inline menu"
    )


@user_router.callback_query(F.data == "category_market_cap_change_24h_desc")
async def inline_categories_market_change_button(query: CallbackQuery) -> str:
    """
    List all categories sorted by market cap change 24h
    """
    result = await get_categories_list_data("market_cap_change_24h_desc")
    await query.message.edit_text(f"{market_cap_change_24h_category_text}\n\n{result}", reply_markup=cat_kb())
    logger.info(
        f"USER: {query.from_user.full_name} USERNAME: {query.from_user.username} "
        f"ID: {query.from_user.id} getting 'CATEGORIES by market change' inline menu"
    )


# GAS GWEI:
@user_router.message(commands="gas")
async def cmd_gas(message: Message) -> str:
    """
    Get GAS (Gwei) menu
    Usage: /gas command
    """
    await message.delete()
    result = await gas_tracker()
    await message.answer(result, reply_markup=bmm_kb(), disable_web_page_preview = True)
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} getting 'GAS' data"
    )


@user_router.callback_query(F.data == "gas_gwei")
async def inline_coins_button(query: CallbackQuery) -> str:
    """
    Get GAS (Gwei) menu
    Usage: press [Gas] button
    """
    result = await gas_tracker()
    await query.message.edit_text(result, reply_markup=bmm_kb(), disable_web_page_preview = True)
    logger.info(
        f"USER: {query.from_user.full_name} USERNAME: {query.from_user.username} "
        f"ID: {query.from_user.id} getting 'GAS' data"
    )


@user_router.message(F.content_type.in_("sticker"))
async def echo_sticker(message: Message):
    stickers = [
        "CAACAgIAAxkBAAEPi-NibZ_5LwRhCcqyU9XpvEWqpGcIWwACOxEAAsHXqEvBYkQhS-j1IiQE",
        "CAACAgIAAxkBAAEPi-tibaGEA9GyAAFAINLKq3yN-fVlQSUAAr4WAAJFIyBLGWV2Y6eXgvwkBA",
        "CAACAgIAAxkBAAEPi_NibaVI8atcEhxY1OkUzR0JLGQQ6QACSxcAAkCuoEvJU2dSezl_IyQE",
        "CAACAgIAAxkBAAEPi_VibaVYJBBr9Imlhq2rPhWZP5lEewAC7BUAAsymwUuIP6qzCm_qWSQE",
        "CAACAgIAAxkBAAEPi_dibaVshu26cCgCYrnTdR1xsDPptAACzhMAAsspqUvRpYTRVOh2_yQE",
        "CAACAgIAAxkBAAEPi_libaWBBJb8JTRBOslh9CMPsmkxVAACCBMAAuYzqUvMsnvh0yHD5CQE",
        "CAACAgIAAxkBAAEPi_tibaWRB_imXo6myPTnGIBC-XL9cwACWRkAAgSzIUtj64Ra50Z_VSQE",
        "CAACAgIAAxkBAAEPi_1ibaWiO1ZECu2bIQcBwI3rp-dSpwACpBUAAqNkIUvTUiowo_kd6CQE",
        "CAACAgIAAxkBAAEPi_9ibaW64UTZPmwFBRznR3wqLI9rZwACvhYAAkUjIEsZZXZjp5eC_CQE"
    ]
    await message.answer_sticker(sticker=choice(stickers))


# ADDITIONAL BACK BUTTON
@user_router.callback_query(F.data == "back_to_main_menu")
async def back_button(query: CallbackQuery) -> str:
    """
    Back to main menu with inline button
    Usage: press [Main menu] button
    """
    await query.message.edit_text(main_text, reply_markup=main_kb(), disable_web_page_preview=True)
    logger.info(
        f"USER: {query.from_user.full_name} USERNAME: {query.from_user.username} "
        f"ID: {query.from_user.id} getting 'MAIN MENU'"
    )


# Testing user_router
@user_router.message(commands="user", flags=flags)
async def cmd_user(message: Message) -> str:
    await message.answer("This is a router for users")