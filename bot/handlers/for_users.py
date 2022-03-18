from aiogram import Router
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
# from aiogram.dispatcher.fsm.context import FSMContext TODO

from handlers.coingecko.coins import token_id, token_name, trend
from handlers.coingecko.cg_categories import cg_categories

from api_requests.coingecko.token_json import csv_keys, csv_values
from api_requests.coingecko.token_json import cg_categories_values
from data.text_file import help_text, coins_text, categories_text

from keypads.keyboards import (
    get_main_keyboard as main_kb,
    get_coin_inline_keyboard as coin_kb,
    get_categories_inline_keyboard as cat_kb
)

user_router = Router()


@user_router.message(commands="user")
async def cmd_test2(message: Message) -> str:
    await message.answer("This is a router for users")


async def cmd_help(message: Message) -> str:
    """
    /HELP bot command
    """
    await message.answer(help_text)


async def cmd_coins(message: Message) -> str:
    """
    /COINS bot command
    """
    await message.answer(coins_text, reply_markup=coin_kb())


async def cmd_categories(message: Message) -> str:
    """
    /CATEGORIES bot command
    """
    await message.answer(categories_text, reply_markup=cat_kb())


async def cmd_start(message: Message) -> str:
    """
    /START bot command
    """
    start_text = (
        f'<b>{message.from_user.first_name}, добро пожаловать в CryptoApe сообщество!</b>\n'
        'Бот создан помочь отслеживать цены на криптоактивы.\n\n'
        'Меню команд - /help'
    )
    await message.answer(start_text, reply_markup=main_kb()) # , parse_mode=types.ParseMode.HTML


async def echo(message: Message) -> str:
    """
    ECHO message
    """
    echo_text = (
        '<b>Команда не опознана!</b>\n'
        'Ваше сообщение:\n'
        f'{message.text}\n\n'
        '<b>Используйте</b> /help'
    )
    await message.answer(echo_text)


def register_commands(router: Router):
    # flags = {"throttling_key": "default"} TODO
    router.message.register(cmd_start, Command(commands={'start', 'restart'})) #, flags=flags
    router.message.register(cmd_help, Command(commands="help"))
    router.message.register(cmd_coins, commands='coins')
    router.message.register(cmd_categories, commands='categories')
    router.message.register(trend, commands='trend')
    router.message.register(token_name, commands=csv_keys)  # search tokens by name
    router.message.register(token_id, commands=csv_values)  # search tokens by symbol
    router.message.register(cg_categories, commands=cg_categories_values)
    router.message.register(echo)


# TODO
# # v2 aio Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f'Эхо в состоянии <code>{state}</code>.\n'
#                          f'\nСодержание сообщения: '
#                          f'\n<code>{message}</code>')