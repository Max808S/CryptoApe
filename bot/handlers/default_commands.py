import secrets

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from data.text_file import (
    help_text, coins_text, categories_text, disclaimer, main_text
)

from keypads.keyboards import (
    get_main_keyboard as main_kb,
    get_coin_inline_keyboard as coin_kb,
    get_categories_inline_keyboard as cat_kb
)


flags = {"throttling_key": "default"}
user_router = Router(name=__name__)


# MENU BUTTONS:
@user_router.message(F.text == "Монеты")
async def coins_button(message: Message) -> None:
    await message.answer(coins_text, reply_markup=coin_kb())


@user_router.message(F.text == "Категории")
async def categories_button(message: Message) -> None:
    await message.answer(categories_text, reply_markup=cat_kb())


# INLINE MENU BUTTONS:
@user_router.callback_query(F.data == "coins")
async def inline_coins_button(query: CallbackQuery) -> str:
    await query.message.edit_text(coins_text)
    await query.message.edit_reply_markup(reply_markup=coin_kb())


@user_router.callback_query(F.data == "categories")
async def inline_categories_button(query: CallbackQuery) -> str:
    await query.message.edit_text(categories_text)
    await query.message.edit_reply_markup(reply_markup=cat_kb())
    

@user_router.callback_query(F.data == "back_to_main_menu")
async def back_button(query: CallbackQuery) -> str:
    await query.message.edit_text(main_text)
    await query.message.edit_reply_markup(reply_markup=main_kb())


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
    await message.answer(help_text)


@user_router.message(commands="coins")
async def cmd_coins(message: Message) -> str:
    """
    /COINS bot command
    """
    await message.delete()
    await message.answer(coins_text, reply_markup=coin_kb())


@user_router.message(commands="categories")
async def cmd_categories(message: Message) -> str:
    """
    /CATEGORIES bot command
    """
    await message.delete()
    await message.answer(categories_text, reply_markup=cat_kb())


# EDITOR TESTING
@user_router.callback_query(F.data == "test")
async def inline_test_button(query: CallbackQuery) -> str:
    await query.message.edit_text(text=secrets.token_urlsafe(4))
    await query.message.edit_reply_markup(reply_markup=main_kb())


@user_router.message(commands="user", flags=flags)
async def cmd_user(message: Message) -> str:
    await message.answer("This is a router for users")