from aiogram import Router
from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from textwrap import dedent


# NFT menu
async def cmd_opensea(message: Message):
    start_text = f"""\
        <b>Топ OpenSea NFT коллекции</b>
        
        Меню команд - /help
        """
    await message.answer(dedent(start_text)) # , parse_mode=types.ParseMode.HTML


def register_opensea(router: Router):
    router.message.register(cmd_opensea, Command(commands="opensea"))





# # menu for every category
# @dp.callback_query_handler(text='nft_collections_menu')
# async def get_back_menu(self: types.Message):
#     await bot.send_message(self.from_user.id, 'Выбери коллекцию которую хочешь посмотреть \U0001F4B0',
#                         reply_markup=nft_collections_menu)

# @dp.callback_query_handler(text='crypto_punks')
# async def crypto_punks_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('cryptopunks', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)

# @dp.callback_query_handler(text='bored_ape_yacht_club')
# async def bayc_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('boredapeyachtclub', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)

# @dp.callback_query_handler(text='hape_prime')
# async def hapeprime_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('hapeprime', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)

# @dp.callback_query_handler(text='cool_cats_nft')
# async def cool_cats_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('cool-cats-nft', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)

# @dp.callback_query_handler(text='mutant_ape_yacht_club')
# async def mayc_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('mutant-ape-yacht-club', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)

# @dp.callback_query_handler(text='doodles')
# async def doodles_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('doodles-official', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)

# @dp.callback_query_handler(text='deadfellaz')
# async def deadfellaz_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('deadfellaz', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)

# @dp.callback_query_handler(text='cyberkongz')
# async def cyberkongz_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('cyberkongz', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)

# @dp.callback_query_handler(text='mekaverse')
# async def mekaverse_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('mekaverse', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)

# @dp.callback_query_handler(text='alienfrensnft')
# async def alienfrensnft_info(self: types.Message):
#     await bot.delete_message(self.from_user.id, self.message.message_id)
#     await bot.send_message(self.from_user.id, 
#     CollectionStat('alienfrensnft', self.from_user.username, self.from_user.id), 
#     reply_markup=back_nft_menu)