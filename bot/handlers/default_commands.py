from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from api_requests.coingecko import get_categories_list, get_categories_list_data
from api_requests.gas_gwei import gas_tracker

from data.text_file import (
    help_text, coins_text, disclaimer, main_text,
    category_text, market_cap_category_text, market_cap_change_24h_category_text
)

from keypads.keyboards import (
    get_main_keyboard as main_kb,
    get_coin_inline_keyboard as coin_kb,
    get_categories_inline_keyboard as cat_kb,
    get_full_categories_inline_keyboard as full_cat,
    get_back_main_menu_keyboards as bmm_kb
)


flags = {"throttling_key": "default"}
user_router = Router(name=__name__)


# MAIN BOT COMMANDS:
@user_router.message(commands={"start", "restart"}, flags=flags)
async def cmd_start(message: Message) -> str:
    """
    /START bot command
    """
    start_sticker = "CAACAgIAAxkBAAEO47NiOinvXVKHDyUd9W2lVS9186mXigACVAADQbVWDGq3-McIjQH6IwQ"
    start_text = (
        f'<b>{message.from_user.first_name}, добро пожаловать в CryptoApe сообщество!</b>\n\n'
        f'{disclaimer}'
    )
    await message.answer_sticker(sticker=start_sticker)
    await message.answer(
        start_text, 
        disable_web_page_preview = True, 
        reply_markup=main_kb()
    )


@user_router.message(commands="help", flags=flags)
async def cmd_help(message: Message) -> str:
    """
    /HELP bot command
    """
    await message.delete()
    await message.answer("🤖")
    await message.answer(help_text, disable_web_page_preview=True)


@user_router.message(commands="coins")
async def cmd_coins(message: Message) -> str:
    """
    /COINS bot command
    """
    await message.delete()
    await message.answer("💎")
    await message.answer(coins_text, reply_markup=coin_kb())


# INLINE MENU BUTTONS:
@user_router.callback_query(F.data == "coins")
async def inline_coins_button(query: CallbackQuery) -> str:
    await query.message.edit_text(coins_text)
    await query.message.edit_reply_markup(reply_markup=coin_kb())


@user_router.callback_query(F.data == "back_to_main_menu")
async def back_button(query: CallbackQuery) -> str:
    await query.message.edit_text(main_text)
    await query.message.edit_reply_markup(reply_markup=main_kb())


# CATEGORIES
@user_router.message(commands="categories")
async def cmd_categories(message: Message) -> str:
    """
    Get category menu with /categories command
    """
    await message.delete()
    await message.answer("📂")
    await message.answer(category_text, reply_markup=cat_kb())


@user_router.callback_query(F.data == "categories")
async def inline_categories_button(query: CallbackQuery) -> str:
    """
    Get category menu with inline button
    """
    await query.message.edit_text(category_text)
    await query.message.edit_reply_markup(reply_markup=cat_kb())


@user_router.callback_query(F.data == "full_categories")
async def inline_full_categories_button(query: CallbackQuery) -> str:
    """
    List all categories
    """
    result = await get_categories_list()
    await query.message.edit_text(result)
    await query.message.edit_reply_markup(reply_markup=full_cat())
       

# categories: market_cap_desc
@user_router.callback_query(F.data == "category_market_cap_desc")
async def inline_categories_market_cap_button(query: CallbackQuery) -> str:
    """
    List all categories sorted by market cap
    """
    result = await get_categories_list_data("market_cap_desc")
    await query.message.edit_text(f"{market_cap_category_text}\n\n{result}")
    await query.message.edit_reply_markup(reply_markup=cat_kb())


# categories: market_cap_change_24h_desc
@user_router.callback_query(F.data == "category_market_cap_change_24h_desc")
async def inline_categories_market_change_button(query: CallbackQuery) -> str:
    """
    List all categories sorted by market cap change 24h
    """
    result = await get_categories_list_data("market_cap_change_24h_desc")
    await query.message.edit_text(f"{market_cap_change_24h_category_text}\n\n{result}")
    await query.message.edit_reply_markup(reply_markup=cat_kb())


# GAS GWEI
@user_router.message(commands="gas")
async def cmd_gas(message: Message) -> str:
    """
    /GAS bot command
    """
    await message.delete()
    result = await gas_tracker()
    await message.answer(result, reply_markup=bmm_kb(), disable_web_page_preview = True)


@user_router.callback_query(F.data == "gas_gwei")
async def inline_coins_button(query: CallbackQuery) -> str:
    result = await gas_tracker()
    await query.message.edit_text(result, disable_web_page_preview = True)
    await query.message.edit_reply_markup(reply_markup=bmm_kb())


# Testing user_router
@user_router.message(commands="user", flags=flags)
async def cmd_user(message: Message) -> str:
    await message.answer("This is a router for users")