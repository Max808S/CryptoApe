# from aiogram import Bot
# from aiogram.types import BotCommand, BotCommandScopeDefault
# from handlers.default_commands import *
# from loader import *

###   TODO    ###


# bot.set_my_commands(
#     commands=
#     [
#         BotCommand({'start', 'restart'}, 'welcome text'),
#         BotCommand('help', 'Справочная информация')
#     ]
# )
    # await bot.set_my_commands(commands=commands)


# async def set_bot_commands(bot: Bot):
#     data = [
#         (
#             [
#                 BotCommand(command={"start","restart"}, description="Start"),
#                 BotCommand(command="help", description="How to use CrypoCat?")
#             ],
#             BotCommandScopeDefault(),
#             None
#         )
#     ]
#     for commands_list, commands_scope, language in data:
#         await bot.set_my_commands(commands=commands_list, scope=commands_scope, language_code=language)