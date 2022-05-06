from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.dispatcher.filters.callback_data import CallbackData
from typing import Optional


class CGSeachFactory(CallbackData, prefix="cgsearch"):
    action: str
    value: Optional[str]


class RefreshCoinFactory(CallbackData, prefix="refresh_coin"):
    action: str
    value: Optional[str]


class CGTokenFactory(CallbackData, prefix="token"):
    action: str
    value: Optional[str]


def get_main_coins_keyboard() -> InlineKeyboardMarkup:
    """
    Main menu coins button 
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="BTC", callback_data=CGTokenFactory(action="cgtoken", value="bitcoin"))
    builder.button(text="ETH", callback_data=CGTokenFactory(action="cgtoken", value="ethereum"))
    builder.button(text="BNB", callback_data=CGTokenFactory(action="cgtoken", value="binancecoin"))
    builder.button(text="SOL", callback_data=CGTokenFactory(action="cgtoken", value="solana"))
    builder.button(text="DOT", callback_data=CGTokenFactory(action="cgtoken", value="polkadot"))

    builder.button(text="XRP", callback_data=CGTokenFactory(action="cgtoken", value="ripple"))
    builder.button(text="ADA", callback_data=CGTokenFactory(action="cgtoken", value="cardano"))
    builder.button(text="LUNA", callback_data=CGTokenFactory(action="cgtoken", value="terra-luna"))
    builder.button(text="AVAX", callback_data=CGTokenFactory(action="cgtoken", value="avalanche-2"))
    builder.button(text="DOGE", callback_data=CGTokenFactory(action="cgtoken", value="dogecoin"))

    builder.button(text="MATIC", callback_data=CGTokenFactory(action="cgtoken", value="matic-network"))
    builder.button(text="LINK", callback_data=CGTokenFactory(action="cgtoken", value="chainlink"))
    builder.button(text="NEAR", callback_data=CGTokenFactory(action="cgtoken", value="near"))
    builder.button(text="LTC", callback_data=CGTokenFactory(action="cgtoken", value="litecoin"))
    builder.button(text="TRX", callback_data=CGTokenFactory(action="cgtoken", value="tron"))

    builder.button(text="XLM", callback_data=CGTokenFactory(action="cgtoken", value="stellar"))
    builder.button(text="VET", callback_data=CGTokenFactory(action="cgtoken", value="vechain"))
    builder.button(text="SAND", callback_data=CGTokenFactory(action="cgtoken", value="the-sandbox"))
    builder.button(text="GALA", callback_data=CGTokenFactory(action="cgtoken", value="gala"))
    builder.button(text="OASIS", callback_data=CGTokenFactory(action="cgtoken", value="oasis-network"))

    builder.button(text="TON", callback_data=CGTokenFactory(action="cgtoken", value="the-open-network"))
    builder.button(text="APE", callback_data=CGTokenFactory(action="cgtoken", value="apecoin"))
    builder.button(text="ALGO", callback_data=CGTokenFactory(action="cgtoken", value="algorand"))
    builder.button(text="XMR", callback_data=CGTokenFactory(action="cgtoken", value="monero"))
    builder.button(text="EOS", callback_data=CGTokenFactory(action="cgtoken", value="eos"))

    builder.button(text="Категории", callback_data="categories")
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    builder.adjust(5)
    return builder.as_markup()


def get_advanced_search_keyboard(query: str) -> InlineKeyboardMarkup:
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


def get_refresh_coin_keyboard(query: str) -> InlineKeyboardMarkup:
    """
    Refresh coin stat
    """
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Обновить", callback_data=RefreshCoinFactory(action="refresh", value=query)
    )
    builder.button(
        text="Главное меню", callback_data="back_to_main_menu")
    return builder.as_markup()


def get_back_main_menu_keyboards() -> InlineKeyboardMarkup:
    """
    Get /btc /ltc /idt inline buttons
    """
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Главное меню", callback_data="back_to_main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_extra_categories_keyboards() -> InlineKeyboardMarkup:
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


def get_extra_coins_keyboards() -> InlineKeyboardMarkup:
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


def get_main_keyboard() -> InlineKeyboardMarkup:
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


def get_categories_inline_keyboard() -> InlineKeyboardMarkup:
    """
    Get /categories keyboard buttons
    """
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Капитализация', callback_data='category_market_cap_desc'),
            InlineKeyboardButton(text='Изменения за 24ч', callback_data='category_market_cap_change_24h_desc')
        ],
        [
            InlineKeyboardButton(text="Все категории", callback_data="full_categories"),
            InlineKeyboardButton(text="Главное меню", callback_data="back_to_main_menu")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_full_categories_inline_keyboard() -> InlineKeyboardMarkup:
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


# def test_keyboard(currencies: list):
#     inline_keyboard = [
#         [
#             InlineKeyboardButton(text=each, callback_data=each) for each in currencies
#         ]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)