from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.dispatcher.filters.callback_data import CallbackData   # TODO


def get_main_keyboard() -> None:
    """
    /start menu
    """
    keyboard = [
        [KeyboardButton(text='Монеты'), KeyboardButton(text='OpenSea'), KeyboardButton(text='Газ')],    # row 1
        [KeyboardButton(text='Биржи'), KeyboardButton(text='Алерт'), KeyboardButton(text='Категории')]     # row 2        
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def coins_menu_keyboard() -> None:
    """
    /coins menu
    """
    coins_board = [
        [KeyboardButton(text='BTC'), KeyboardButton(text='ETH'), KeyboardButton(text='BNB'), 
        KeyboardButton(text='SOL'), KeyboardButton(text='DOT')],    # row 1
        [KeyboardButton(text='XRP'), KeyboardButton(text='ADA'), KeyboardButton(text='LUNA'), 
        KeyboardButton(text='AVAX'), KeyboardButton(text='DOGE')],    # row 2
        [KeyboardButton(text='MATIC'), KeyboardButton(text='LINK'), KeyboardButton(text='NEAR'), 
        KeyboardButton(text='LTC'), KeyboardButton(text='TRX')],    # row 3
        [KeyboardButton(text='XLM'), KeyboardButton(text='VET'), KeyboardButton(text='SAND'), 
        KeyboardButton(text='GALA'), KeyboardButton(text='OASIS')],    # row 4
    ]
    return ReplyKeyboardMarkup(keyboard=coins_board, resize_keyboard=True)


# testing
def coins_menu_inline_keyboard() -> None:
    inline_board =[
        [
            InlineKeyboardButton(text='BTC', callback_data='/btc'), 
            InlineKeyboardButton(text='ETH', callback_data='/eth'), 
            InlineKeyboardButton(text='BNB', callback_data='/bnb'), 
            InlineKeyboardButton(text='SOL', callback_data='/sol'), 
            InlineKeyboardButton(text='DOT', callback_data='/dot')
            ],
        [
            InlineKeyboardButton(text='XRP', callback_data='/xrp'),
            InlineKeyboardButton(text='ADA', callback_data='/ada'),
            InlineKeyboardButton(text='LUNA', callback_data='/luna'),
            InlineKeyboardButton(text='AVAX', callback_data='/avax'),
            InlineKeyboardButton(text='DOGE', callback_data='/doge')
            ],
        [
            InlineKeyboardButton(text='MATIC', callback_data='/matic'),
            InlineKeyboardButton(text='LINK', callback_data='/link'),
            InlineKeyboardButton(text='NEAR', callback_data='/near'),
            InlineKeyboardButton(text='LTC', callback_data='/ltc'),
            InlineKeyboardButton(text='TRX', callback_data='/trx')
            ],
        [
            InlineKeyboardButton(text='XLM', callback_data='/xlm'),
            InlineKeyboardButton(text='VET', callback_data='/vet'),
            InlineKeyboardButton(text='SAND', callback_data='/sand'),
            InlineKeyboardButton(text='GALA', callback_data='/gala'),
            InlineKeyboardButton(text='OASIS', callback_data='/oasis')
            ]
        ]
    return InlineKeyboardMarkup(inline_keyboard=inline_board)


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
