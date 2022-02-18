from aiogram import types, Dispatcher
from textwrap import dedent

from keypads.keyboards import keyboard as kb


# START command
async def cmd_start(event: types.Message):
    start_text = f"""\
        <b>{event.from_user.get_mention(as_html=True)}, добро пожаловать в CryptoCat сообщество!</b>
        Бот создан помочь отслеживать цены на криптоактивы.
        
        Меню команд - /help
        """
    await event.answer(dedent(start_text), parse_mode=types.ParseMode.HTML, reply_markup=kb)


# HELP command
async def cmd_help(event: types.Message):
    help_text = f"""\
        Crypto Bot Help Menu:

        /coins - посмотреть монеты
        /notify - установить уведомление
        /exchanges - посмотреть биржи
        /opensea - nft коллекции
        /gas - стоимость транзакций на ефире
        /restart - перезагрузить бота
        """
    await event.answer(dedent(help_text))


# ECHO message
async def echo(message: types.Message):
    await message.answer(f'Команда не опознана!'
                         f'\nВаше сообщение:  '
                         f'\n{message.text}'
                         f'\nИспользуйте /help')



def register_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands={'start', 'restart', 'rst'})
    dp.register_message_handler(cmd_help, commands='help')
    dp.register_message_handler(echo)