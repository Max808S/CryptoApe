from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

import secrets # testing


def get_back_main_menu_keyboards():
    """
    Get /btc /ltc /idt inline buttons
    """
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Главное меню", callback_data="back_to_main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_extra_categories_keyboards():
    """
    Get extra categories inline buttons
    """
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Категории", callback_data="categories"),
            InlineKeyboardButton(text="Главное меню", callback_data="back_to_main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_extra_coins_keyboards():
    """
    /btc /ltc /idt inline buttons
    """
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Назад", callback_data="coins"),
            InlineKeyboardButton(text="Главное меню", callback_data="back_to_main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_main_keyboard() -> None:
    """
    /start menu
    """
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Монеты", callback_data="coins"),
            InlineKeyboardButton(text="Категории", callback_data="categories")
        ],
        [
            InlineKeyboardButton(text="Тренд", callback_data="trend"),
            InlineKeyboardButton(text=secrets.token_urlsafe(4), callback_data="test")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_categories_inline_keyboard() -> None:
    """
    Get /categories keyboard buttons
    """
    inline_keyboard = [
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
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_coin_inline_keyboard() -> None:
    """
    Get /coin keyboard buttons
    """
    inline_keyboard = [
        [
            InlineKeyboardButton(text='BTC', callback_data='btc'), 
            InlineKeyboardButton(text='ETH', callback_data='eth'), 
            InlineKeyboardButton(text='BNB', callback_data='bnb'), 
            InlineKeyboardButton(text='SOL', callback_data='sol'), 
            InlineKeyboardButton(text='DOT', callback_data='dot')
        ],
        [
            InlineKeyboardButton(text='XRP', callback_data='xrp'),
            InlineKeyboardButton(text='ADA', callback_data='ada'),
            InlineKeyboardButton(text='LUNA', callback_data='luna'),
            InlineKeyboardButton(text='AVAX', callback_data='avax'),
            InlineKeyboardButton(text='DOGE', callback_data='doge')
        ],
        [
            InlineKeyboardButton(text='MATIC', callback_data='matic'),
            InlineKeyboardButton(text='LINK', callback_data='link'),
            InlineKeyboardButton(text='NEAR', callback_data='near'),
            InlineKeyboardButton(text='LTC', callback_data='ltc'),
            InlineKeyboardButton(text='TRX', callback_data='trx')
        ],
        [
            InlineKeyboardButton(text='XLM', callback_data='xlm'),
            InlineKeyboardButton(text='VET', callback_data='vet'),
            InlineKeyboardButton(text='SAND', callback_data='sand'),
            InlineKeyboardButton(text='GALA', callback_data='gala'),
            InlineKeyboardButton(text='OASIS', callback_data='oasis')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)