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


class CoinRateFactory(CallbackData, prefix="rate"):
    action: str
    value: Optional[str]


class MarketCapFactory(CallbackData, prefix="market_cap"):
    action: str
    value: Optional[int]


class TotalVolumeFactory(CallbackData, prefix="total_volume"):
    action: str
    value: Optional[int]


class H1_Factory(CallbackData, prefix="h1_factory"):
    action: str
    value: Optional[int]


class H24_Factory(CallbackData, prefix="h24_factory"):
    action: str
    value: Optional[int]


class D7_Factory(CallbackData, prefix="d7_factory"):
    action: str
    value: Optional[int]


class GainersLosersFactory(CallbackData, prefix="gainers_losers"):
    action: str
    value: Optional[str]


def get_setting_menu_keyboards() -> InlineKeyboardMarkup:
    """
    Get setting menu.
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="Язык", callback_data="language")
    builder.button(text="Валюта", callback_data="currency")
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    
    builder.adjust(2)
    return builder.as_markup()


def get_currency_menu_keyboards() -> InlineKeyboardMarkup:
    """
    Get currency setting menu.
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="USD", callback_data="usd_currency")
    builder.button(text="EUR", callback_data="eur_currency")
    builder.button(text="RUB", callback_data="rub_currency")
    builder.button(text="UAH", callback_data="uah_currency")

    builder.button(text="< Назад", callback_data="setting")
    
    builder.adjust(4)
    return builder.as_markup()


def get_language_menu_keyboards() -> InlineKeyboardMarkup:
    """
    Get language setting menu.
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="ENG", callback_data="eng_language")
    builder.button(text="RUS", callback_data="rus_language")

    builder.button(text="< Назад", callback_data="setting")
    
    builder.adjust(2)
    return builder.as_markup()


# def get_extra_stat_menu_keyboards() -> InlineKeyboardMarkup:
#     inline_keyboard = [
#         [
#             InlineKeyboardButton(text="< Назад", callback_data="tokens_view"),
#             InlineKeyboardButton(text="Главное меню", callback_data="back_to_main_menu")
#         ]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_gainers_losers_1h_stat_menu_keyboards() -> InlineKeyboardMarkup:
    """
    Gainer Losers
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="1ч ❇️", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="24ч", callback_data=GainersLosersFactory(action="gainers_losers", value="24h"))
    builder.button(text="7д", callback_data=GainersLosersFactory(action="gainers_losers", value="7d"))
        
    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="1ч  /  24ч  /  7д", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    
    builder.adjust(3, 2, 2)
    return builder.as_markup()


def get_gainers_losers_24h_stat_menu_keyboards() -> InlineKeyboardMarkup:
    """
    Gainer Losers
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="1ч", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="24ч ❇️", callback_data=GainersLosersFactory(action="gainers_losers", value="24h"))
    builder.button(text="7д", callback_data=GainersLosersFactory(action="gainers_losers", value="7d"))
        
    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="Рост / Падение", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    
    builder.adjust(3, 2, 2)
    return builder.as_markup()


def get_gainers_losers_7d_stat_menu_keyboards() -> InlineKeyboardMarkup:
    """
    Gainer Losers
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="1ч", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="24ч", callback_data=GainersLosersFactory(action="gainers_losers", value="24h"))
    builder.button(text="7д ❇️", callback_data=GainersLosersFactory(action="gainers_losers", value="7d"))
        
    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="Рост / Падение", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    
    builder.adjust(3, 2, 2)
    return builder.as_markup()


def get_market_cap_stats_menu_keyboards() -> InlineKeyboardMarkup:
    """
    MarketCap [1 - 2 - 3 - 4 - 5]
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="1", callback_data=MarketCapFactory(action="market_cap_page", value=1))
    builder.button(text="2", callback_data=MarketCapFactory(action="market_cap_page", value=2))
    builder.button(text="3", callback_data=MarketCapFactory(action="market_cap_page", value=3))
    builder.button(text="4", callback_data=MarketCapFactory(action="market_cap_page", value=4))
    builder.button(text="5", callback_data=MarketCapFactory(action="market_cap_page", value=5))
    builder.button(text=">", callback_data=MarketCapFactory(action="market_cap_page", value=6))
    
    builder.button(text="Капитализация ❇️", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    builder.button(text="Рост / Падение", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    
    builder.adjust(6, 1, 2, 2)
    return builder.as_markup()


def get_extra_market_cap_stats_menu_keyboards() -> InlineKeyboardMarkup:
    """
    MarketCap [6 - 7 - 8 - 9 - 10]
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="<", callback_data=MarketCapFactory(action="market_cap_page", value=5))
    builder.button(text="6", callback_data=MarketCapFactory(action="market_cap_page", value=6))
    builder.button(text="7", callback_data=MarketCapFactory(action="market_cap_page", value=7))
    builder.button(text="8", callback_data=MarketCapFactory(action="market_cap_page", value=8))
    builder.button(text="9", callback_data=MarketCapFactory(action="market_cap_page", value=9))
    builder.button(text="10", callback_data=MarketCapFactory(action="market_cap_page", value=10))

    builder.button(text="Капитализация ❇️", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="Рост / Падение", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")

    builder.adjust(6, 1, 2, 2)
    return builder.as_markup()


def get_volume_stats_menu_keyboards() -> InlineKeyboardMarkup:
    """
    VOLUME [1 - 2 - 3 - 4 - 5]
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="1", callback_data=TotalVolumeFactory(action="volume_page", value=1))
    builder.button(text="2", callback_data=TotalVolumeFactory(action="volume_page", value=2))
    builder.button(text="3", callback_data=TotalVolumeFactory(action="volume_page", value=3))
    builder.button(text="4", callback_data=TotalVolumeFactory(action="volume_page", value=4))
    builder.button(text="5", callback_data=TotalVolumeFactory(action="volume_page", value=5))
    builder.button(text=">", callback_data=TotalVolumeFactory(action="volume_page", value=6))

    builder.button(text="Объем торгов ❇️", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Рост / Падение", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")

    builder.adjust(6, 1, 2, 2)
    return builder.as_markup()


def get_extra_volume_stats_menu_keyboards() -> InlineKeyboardMarkup:
    """
    VOLUME [6 - 7 - 8 - 9 - 10]
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="<", callback_data=TotalVolumeFactory(action="volume_page", value=5))
    builder.button(text="6", callback_data=TotalVolumeFactory(action="volume_page", value=6))
    builder.button(text="7", callback_data=TotalVolumeFactory(action="volume_page", value=7))
    builder.button(text="8", callback_data=TotalVolumeFactory(action="volume_page", value=8))
    builder.button(text="9", callback_data=TotalVolumeFactory(action="volume_page", value=9))
    builder.button(text="10", callback_data=TotalVolumeFactory(action="volume_page", value=10))

    builder.button(text="Объем торгов ❇️", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Рост / Падение", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))    
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")

    builder.adjust(6, 1, 2, 2)
    return builder.as_markup()


def get_1h_tokens_stat_menu_keyboards() -> InlineKeyboardMarkup:
    """
    1h
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="1", callback_data=H1_Factory(action="h1_list", value=1))
    builder.button(text="2", callback_data=H1_Factory(action="h1_list", value=2))
    builder.button(text="3", callback_data=H1_Factory(action="h1_list", value=3))
    builder.button(text="4", callback_data=H1_Factory(action="h1_list", value=4))
    builder.button(text="5", callback_data=H1_Factory(action="h1_list", value=5))
    builder.button(text=">", callback_data=H1_Factory(action="h1_list", value=6))

    builder.button(text="1ч ❇️", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    builder.button(text="24ч", callback_data=CoinRateFactory(action="cgrate", value="h24_result"))
    builder.button(text="7д", callback_data=CoinRateFactory(action="cgrate", value="d7_result"))

    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    
    builder.adjust(6, 3, 2, 2)
    return builder.as_markup()


def get_extra_1h_tokens_stat_menu_keyboards() -> InlineKeyboardMarkup:
    """
    1h extra
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="<", callback_data=H1_Factory(action="h1_list", value=5))
    builder.button(text="6", callback_data=H1_Factory(action="h1_list", value=6))
    builder.button(text="7", callback_data=H1_Factory(action="h1_list", value=7))
    builder.button(text="8", callback_data=H1_Factory(action="h1_list", value=8))
    builder.button(text="9", callback_data=H1_Factory(action="h1_list", value=9))
    builder.button(text="10", callback_data=H1_Factory(action="h1_list", value=10))

    builder.button(text="1ч ❇️", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    builder.button(text="24ч", callback_data=CoinRateFactory(action="cgrate", value="h24_result"))
    builder.button(text="7д", callback_data=CoinRateFactory(action="cgrate", value="d7_result"))

    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    
    builder.adjust(6, 3, 2, 2)
    return builder.as_markup()


def get_24h_tokens_stat_menu_keyboards() -> InlineKeyboardMarkup:
    """
    24h
    """
    builder = InlineKeyboardBuilder()
    
    builder.button(text="1", callback_data=H24_Factory(action="h24_list", value=1))
    builder.button(text="2", callback_data=H24_Factory(action="h24_list", value=2))
    builder.button(text="3", callback_data=H24_Factory(action="h24_list", value=3))
    builder.button(text="4", callback_data=H24_Factory(action="h24_list", value=4))
    builder.button(text="5", callback_data=H24_Factory(action="h24_list", value=5))
    builder.button(text=">", callback_data=H24_Factory(action="h24_list", value=6))

    builder.button(text="1ч", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    builder.button(text="24ч ❇️", callback_data=CoinRateFactory(action="cgrate", value="h24_result"))
    builder.button(text="7д", callback_data=CoinRateFactory(action="cgrate", value="d7_result"))

    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")

    builder.adjust(6, 3, 2, 2)
    return builder.as_markup()


def get_extra_24h_tokens_stat_menu_keyboards() -> InlineKeyboardMarkup:
    """
    24h extra
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="<", callback_data=H24_Factory(action="h24_list", value=5))
    builder.button(text="6", callback_data=H24_Factory(action="h24_list", value=6))
    builder.button(text="7", callback_data=H24_Factory(action="h24_list", value=7))
    builder.button(text="8", callback_data=H24_Factory(action="h24_list", value=8))
    builder.button(text="9", callback_data=H24_Factory(action="h24_list", value=9))
    builder.button(text="10", callback_data=H24_Factory(action="h24_list", value=10))

    builder.button(text="1ч", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    builder.button(text="24ч ❇️", callback_data=CoinRateFactory(action="cgrate", value="h24_result"))
    builder.button(text="7д", callback_data=CoinRateFactory(action="cgrate", value="d7_result"))

    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    
    builder.adjust(6, 3, 2, 2)
    return builder.as_markup()


def get_7d_tokens_stat_menu_keyboards() -> InlineKeyboardMarkup:
    """
    7d
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="1", callback_data=D7_Factory(action="d7_list", value=1))
    builder.button(text="2", callback_data=D7_Factory(action="d7_list", value=2))
    builder.button(text="3", callback_data=D7_Factory(action="d7_list", value=3))
    builder.button(text="4", callback_data=D7_Factory(action="d7_list", value=4))
    builder.button(text="5", callback_data=D7_Factory(action="d7_list", value=5))
    builder.button(text=">", callback_data=D7_Factory(action="d7_list", value=6))

    builder.button(text="1ч", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    builder.button(text="24ч", callback_data=CoinRateFactory(action="cgrate", value="h24_result"))
    builder.button(text="7д ❇️", callback_data=CoinRateFactory(action="cgrate", value="d7_result"))

    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")

    builder.adjust(6, 3, 2, 2)
    return builder.as_markup()


def get_extra_7d_tokens_stat_menu_keyboards() -> InlineKeyboardMarkup:
    """
    7d extra
    """
    builder = InlineKeyboardBuilder()

    builder.button(text="<", callback_data=D7_Factory(action="d7_list", value=5))
    builder.button(text="6", callback_data=D7_Factory(action="d7_list", value=6))
    builder.button(text="7", callback_data=D7_Factory(action="d7_list", value=7))
    builder.button(text="8", callback_data=D7_Factory(action="d7_list", value=8))
    builder.button(text="9", callback_data=D7_Factory(action="d7_list", value=9))
    builder.button(text="10", callback_data=D7_Factory(action="d7_list", value=10))

    builder.button(text="1ч", callback_data=CoinRateFactory(action="cgrate", value="h1_result"))
    builder.button(text="24ч", callback_data=CoinRateFactory(action="cgrate", value="h24_result"))
    builder.button(text="7д ❇️", callback_data=CoinRateFactory(action="cgrate", value="d7_result"))

    builder.button(text="Капитализация", callback_data=CoinRateFactory(action="cgrate", value="market_cap_desc"))
    builder.button(text="Объем торгов", callback_data=CoinRateFactory(action="cgrate", value="volume_desc"))
    
    builder.button(text="< Назад", callback_data=GainersLosersFactory(action="gainers_losers", value="1h"))
    builder.button(text="Главное меню", callback_data="back_to_main_menu")
    
    builder.adjust(6, 3, 2, 2)
    return builder.as_markup()


def get_main_coins_keyboard() -> InlineKeyboardMarkup:
    """
    Main menu coins button.
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
    Get search keyboard.
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
    Refresh coin stat.
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
            InlineKeyboardButton(text="< Назад", callback_data="coins"),
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
            InlineKeyboardButton(text="Рейтинг", callback_data="ranking")   
        ],
        [
            InlineKeyboardButton(text="Категории", callback_data="categories"),
            InlineKeyboardButton(text="NFT", callback_data="nft_menu")
        ],
        [
            InlineKeyboardButton(text="Тренд", callback_data="trend"),
            InlineKeyboardButton(text="Газ (gwei)", callback_data="gas_gwei")
        ],
        [
            InlineKeyboardButton(text="Уведомления", callback_data="alerts"),
            InlineKeyboardButton(text="Настройки", callback_data="setting")
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