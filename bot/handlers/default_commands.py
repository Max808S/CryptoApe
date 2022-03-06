# from aiogram import types, Dispatcher
from aiogram import Router
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
# from aiogram.dispatcher.fsm.context import FSMContext TODO

from textwrap import dedent
from keypads.keyboards import get_main_keyboard as mk

from api_requests.coingecko.token_json import dict_from_csv, csv_keys, csv_values
from handlers.coingecko.coins import trend, same_def_1, same_def_2


# START command
async def cmd_start(message: Message):
    start_text = f"""\
        <b>{message.from_user.first_name}, добро пожаловать в CryptoCat сообщество!</b>
        Бот создан помочь отслеживать цены на криптоактивы.
        
        Меню команд - /help
        """
    await message.answer(dedent(start_text), reply_markup=mk()) # , parse_mode=types.ParseMode.HTML


# HELP command
async def cmd_help(message: Message):
    help_text = f"""\
        Crypto Bot Help Menu:

        /coins - посмотреть монеты
        /notify - установить уведомление
        /exchanges - посмотреть биржи
        /opensea - nft коллекции
        /gas - стоимость транзакций на ефире
        /restart - перезагрузить бота
        """
    await message.answer(dedent(help_text))


# ECHO message
async def echo(message: Message):
    await message.answer(f'Команда не опознана!'
                         f'\nВаше сообщение:  '
                         f'\n{message.text}'
                         f'\nИспользуйте /help')


# # v2 aio Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f'Эхо в состоянии <code>{state}</code>.\n'
#                          f'\nСодержание сообщения: '
#                          f'\n<code>{message}</code>')


def register_commands(router: Router):
    # flags = {"throttling_key": "default"} TODO
    router.message.register(cmd_start, Command(commands={'start', 'restart'})) #, flags=flags
    router.message.register(cmd_help, Command(commands="help"))
    router.message.register(trend, commands='trend')
    router.message.register(same_def_1, commands=csv_keys)
    router.message.register(same_def_2, commands=csv_values)
    router.message.register(echo)