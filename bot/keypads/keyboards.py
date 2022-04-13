from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.dispatcher.filters.callback_data import CallbackData
from typing import Optional


class CGSeachFactory(CallbackData, prefix="cgsearch"):
    action: str
    value: Optional[str]


def get_advanced_search_keyboard(query: str):
    """
    TODO
    """
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Расширенный поиск", callback_data=CGSeachFactory(action="search", value=query)
    )
    builder.button(
        text="Главное меню", callback_data="back_to_main_menu")
    builder.adjust(1)
    return builder.as_markup()


def get_back_main_menu_keyboards(): # -> InlineKeyboardMarkup
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
            InlineKeyboardButton(text="Газ (gwei)", callback_data="gas_gwei")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_categories_inline_keyboard() -> None:
    """
    Get /categories keyboard buttons
    """
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Капитализация', callback_data='category_market_cap_desc'),
            InlineKeyboardButton(text='Изменения за 24ч', callback_data='category_market_cap_change_24h_desc')
        ],
        # [
        #     InlineKeyboardButton(text='1', callback_data='qwe1'),
        #     InlineKeyboardButton(text='2', callback_data='qwe2'),
        #     InlineKeyboardButton(text='3', callback_data='qwe2'),
        #     InlineKeyboardButton(text='4', callback_data='qwe2'),
        #     InlineKeyboardButton(text='5', callback_data='qwe2')
        # ],
        [
            InlineKeyboardButton(text="Все категории", callback_data="full_categories"),
            InlineKeyboardButton(text="Главное меню", callback_data="back_to_main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_full_categories_inline_keyboard() -> None:
    """
    Get /categories keyboard buttons
    """
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Категории", callback_data="categories"),
            InlineKeyboardButton(text="Главное меню", callback_data="back_to_main_menu")
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
            InlineKeyboardButton(text="Категории", callback_data="categories"),
            InlineKeyboardButton(text="Главное меню", callback_data="back_to_main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


# def test_keyboard(currencies: list):
#     inline_keyboard = [
#         [
#             InlineKeyboardButton(text=each, callback_data=each) for each in currencies
#         ]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)