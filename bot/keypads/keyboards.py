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


def get_categories_inline_keyboard() -> None:
    """
    Get /categories keyboard buttons
    """
    inline_board = [
        [
            InlineKeyboardButton(text='Smart Contract Platform', callback_data='/smart-contract-platform'),
            InlineKeyboardButton(text='BNB Chain Ecosystem', callback_data='/binance-smart-chain')
        ],
        [
            InlineKeyboardButton(text='Polygon Ecosystem', callback_data='/polygon-ecosystem'),
            InlineKeyboardButton(text='Solana Ecosystem', callback_data='/solana-ecosystem')
        ],
        [
            InlineKeyboardButton(text='Meme Tokens', callback_data='/meme-token'),
            InlineKeyboardButton(text='Metaverse', callback_data='/metaverse')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_board)


def get_coin_inline_keyboard() -> None:
    """
    Get /coin keyboard buttons
    """
    inline_board = [
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