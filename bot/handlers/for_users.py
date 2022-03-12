from aiogram import Router
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
# from aiogram.dispatcher.fsm.context import FSMContext TODO

from handlers.coingecko.coins import token_id, token_name, trend
from api_requests.coingecko.token_json import csv_keys, csv_values
from keypads.keyboards import get_main_keyboard as mk
from keypads.keyboards import coins_menu_inline_keyboard as ik

from textwrap import dedent


user_router = Router()


@user_router.message(commands="user")
async def cmd_test2(message: Message):
    await message.answer("This is a router for users")


async def cmd_start(message: Message) -> str:
    """
    /START bot command
    """
    start_text = f"""\
        <b>{message.from_user.first_name}, добро пожаловать в CryptoCat сообщество!</b>
        Бот создан помочь отслеживать цены на криптоактивы.
        
        Посмотреть актуальный прайс монеты, вы можете с помощью команды /btc или /bitcoin (пишите любую монету)
        Меню команд - /help
        """
    await message.answer(dedent(start_text), reply_markup=mk()) # , parse_mode=types.ParseMode.HTML


async def cmd_help(message: Message) -> str:
    """
    /HELP bot command
    """
    help_text = f"""\
        Crypto Bot Help Menu:

        /coins - посмотреть монеты
        /notify - установить уведомление
        /exchanges - посмотреть биржи
        /opensea - nft коллекции
        /gas - стоимость транзакций на ефире
        /restart - перезагрузить бота
        """
    await message.answer(dedent(help_text)) # TODO dedent


async def cmd_coins(message: Message) -> str:
    """
    /COINS bot command
    """
    main_coins_text = (
        f'Выбери монетку которую хочешь посмотреть:'
    )
    await message.answer(main_coins_text, reply_markup=ik())


async def echo(message: Message) -> str:
    """
    ECHO message
    """
    await message.answer(
        f'<b>Команда не опознана!</b>'
        f'\nВаше сообщение:'
        f'\n{message.text}'
        f'\nИспользуйте /help'
        )


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
    router.message.register(cmd_coins, commands='coins')
    router.message.register(trend, commands='trend')
    router.message.register(token_id, commands=csv_keys)
    router.message.register(token_name, commands=csv_values)
    router.message.register(echo)