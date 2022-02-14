from textwrap import dedent
from api_requests.opensea import CollectionStat
from aiogram import types
from loader import *
# from keypads import keyboards as kb
from keypads.keyboards import nft_collections_menu, back_nft_menu



# NFT menu
async def cmd_opensea(event: types.Message):
    start_text = f"""\
        <b>Топ OpenSea NFT коллекции</b>
        
        Меню команд - /help
        """
    await event.answer(dedent(start_text), parse_mode=types.ParseMode.HTML, reply_markup=nft_collections_menu)


def register_opensea(dp: Dispatcher):
    dp.register_message_handler(cmd_opensea, commands='opensea')


# menu for every category
@dp.callback_query_handler(text='nft_collections_menu')
async def get_back_menu(self: types.Message):
    await bot.send_message(self.from_user.id, 'Выбери коллекцию которую хочешь посмотреть \U0001F4B0',
                        reply_markup=nft_collections_menu)

@dp.callback_query_handler(text='crypto_punks')
async def crypto_punks_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('cryptopunks', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)

@dp.callback_query_handler(text='bored_ape_yacht_club')
async def bayc_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('boredapeyachtclub', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)

@dp.callback_query_handler(text='hape_prime')
async def hapeprime_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('hapeprime', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)

@dp.callback_query_handler(text='cool_cats_nft')
async def cool_cats_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('cool-cats-nft', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)

@dp.callback_query_handler(text='mutant_ape_yacht_club')
async def mayc_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('mutant-ape-yacht-club', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)

@dp.callback_query_handler(text='doodles')
async def doodles_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('doodles-official', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)

@dp.callback_query_handler(text='deadfellaz')
async def deadfellaz_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('deadfellaz', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)

@dp.callback_query_handler(text='cyberkongz')
async def cyberkongz_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('cyberkongz', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)

@dp.callback_query_handler(text='mekaverse')
async def mekaverse_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('mekaverse', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)

@dp.callback_query_handler(text='alienfrensnft')
async def alienfrensnft_info(self: types.Message):
    await bot.delete_message(self.from_user.id, self.message.message_id)
    await bot.send_message(self.from_user.id, 
    CollectionStat('alienfrensnft', self.from_user.username, self.from_user.id), 
    reply_markup=back_nft_menu)