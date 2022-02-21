from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> None:
    """
    /start menu
    """
    keyboard = [
        [KeyboardButton(text='Монеты'), KeyboardButton(text='OpenSea'), KeyboardButton(text='Газ')],    # row 1
        [KeyboardButton(text='Биржи'), KeyboardButton(text='Алерт'), KeyboardButton(text='Категории')]     # row 2        
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)




# # OpenSea
# nft_collections_menu = InlineKeyboardMarkup(row_width=1)
# back_nft_menu = InlineKeyboardMarkup(row_width=1)
# back_nft_button = InlineKeyboardButton(text='Назад в коллекции', callback_data='nft_collections_menu')
# back_nft_menu.insert(back_nft_button)


# crypto_punk_button = InlineKeyboardButton(text='Crypto Punks', callback_data='crypto_punks') #cryptopunks
# bayc_button = InlineKeyboardButton(text='Bored Ape Yacht Club', callback_data='bored_ape_yacht_club') # boredapeyachtclub
# hape_prime_button = InlineKeyboardButton(text='Hape Prime', callback_data='hape_prime') # hapeprime
# cool_cat_button = InlineKeyboardButton(text='Cool Cats', callback_data='cool_cats_nft')
# mayc_button = InlineKeyboardButton(text='Mutant Ape Yacht Club', callback_data='mutant_ape_yacht_club') # mutant-ape-yacht-club
# doodles_button = InlineKeyboardButton(text='Doodles', callback_data='doodles') # doodles-official
# deadfellaz_button = InlineKeyboardButton(text='DeadFellaz', callback_data='deadfellaz') # deadfellaz
# cyberkongz_button = InlineKeyboardButton(text='CyberKongz', callback_data='cyberkongz') #cyberkongz
# mekaverse_button = InlineKeyboardButton(text='Mekaverse', callback_data='mekaverse') # mekaverse
# alienfrensnft_button =InlineKeyboardButton(text='Alien Frens', callback_data='alienfrensnft') # alienfrensnft
# # add
# nft_collections_menu.insert(crypto_punk_button)
# nft_collections_menu.insert(bayc_button)
# nft_collections_menu.insert(hape_prime_button)
# nft_collections_menu.insert(cool_cat_button)
# nft_collections_menu.insert(mayc_button)
# nft_collections_menu.insert(doodles_button)
# nft_collections_menu.insert(deadfellaz_button)
# nft_collections_menu.insert(cyberkongz_button)
# nft_collections_menu.insert(mekaverse_button)
# nft_collections_menu.insert(alienfrensnft_button)
