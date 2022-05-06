from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from contextlib import suppress
from misc.logging import logger
from misc.text_file import trend_text

from api_requests.coingecko.coingecko import (
    get_price, get_categories_data, get_trending_coins,
    cg_searcher
)

from api_requests.coingecko.csv_reader import (
    dict_from_tokens_csv, cg_tokens_keys, cg_tokens_values,
    dict_from_cg_categories_csv, cg_categories_values,
    dict_with_token_ids, cg_token_extra_name
)

from keyboards.inline import (
    get_back_main_menu_keyboards as mm_kb,
    get_extra_coins_keyboards as ex_kb,
    get_extra_categories_keyboards as ex_cat_kb,
    get_back_main_menu_keyboards as bmm_kb,
    get_advanced_search_keyboard as adv_search_kb,
    get_refresh_coin_keyboard as ref_kb,
    CGSeachFactory, RefreshCoinFactory, CGTokenFactory
)


coingecko_router = Router(name=__name__)


# TRENDING COINS
@coingecko_router.message(commands="trend")
async def trend(message: types.Message) -> str:
    """
    Get trending search coins (Top-7) on CoinGecko in the last 24 hours.
    /api/v3/search/trending
    """
    await message.delete()
    await message.answer("🌟")
    result = await get_trending_coins()
    full_res = (f'{trend_text}\n\n{result}')
    await message.answer(full_res, reply_markup=mm_kb(), disable_web_page_preview=True)
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} getting 'TREND' menu"
    )


@coingecko_router.callback_query(F.data == "trend")
async def inline_trend_button(query: CallbackQuery):
    result = await get_trending_coins()
    full_res = (f'{trend_text}\n\n{result}')
    await query.message.edit_text(full_res, reply_markup=bmm_kb(), disable_web_page_preview=True)
    logger.info(
        f"USER: {query.from_user.full_name} USERNAME: {query.from_user.username} "
        f"ID: {query.from_user.id} getting 'TREND' inline menu"
    )


# MENU CATEGORIES
@coingecko_router.message(commands=cg_categories_values)
async def cg_categories(message: types.Message):
    """
    Get a list of coins from a category
    """
    await message.delete()
    await message.answer("📂")
    for key, value in dict_from_cg_categories_csv.items():
        if value == message.text[1:]:
            result = await get_categories_data(key)
    await message.answer(result, reply_markup=ex_cat_kb())
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} getting category data for '{message.text[1:]}'"
    )


# SEARCH TOKENS IN CSV BASE: token_name & token_id
@coingecko_router.message(commands=cg_tokens_keys)
async def token_name(message: types.Message):
    """
    Checking the coin in the database (CSV COINS LIST) by name.
    Usage example: /tron-bsc /wrapped-tron
    """
    await message.answer("💱")
    await message.delete()
    result = await get_price(message.text[1:])
    await message.answer(result, reply_markup=ref_kb(message.text[1:]))
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} getting token data for '{message.text[1:]}'"
    )


@coingecko_router.message(commands=cg_token_extra_name)
async def token_extra_id(message: types.Message):
    """
    Checking the coin in the database (CSV COINS LIST) by extra id.
    Example: /tron_bsc /wrapped_tron, bitcoin, solana   /USED: "_"/
    """
    await message.answer("💱")
    await message.delete()
    for key, value in dict_with_token_ids.items():
        if value == message.text[1:]:
            result = await get_price(key)
    await message.answer(result, reply_markup=ref_kb(message.text[1:].replace("_", "-")))
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} getting token data for '{message.text[1:]}'"
    )


@coingecko_router.message(commands=cg_tokens_values)
async def token_id(message: types.Message):
    """
    Create a list if get 2+ coins
    Usage example /SYMBOL/: btc, trx, eth, sol
    """
    coins_id_list = []
    for key, value in dict_from_tokens_csv.items():
        if value == message.text[1:]:
            coins_id_list.append(key)
    await message.delete()
    if len(coins_id_list) >= 2:    
        await message.answer("🔎")
        list_to_str = '\n/'.join([str(elem).replace("-", "_") for elem in coins_id_list])
        result = f"Выберите нужную криптовалюту:\n\n/{list_to_str}"
        await message.answer(result, reply_markup=adv_search_kb(message.text[1:]))
        logger.info(
            f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
            f"ID: {message.from_user.id} getting '{message.text[1:]} SELECTION EXTRA MENU'"
        )
    else:
        await message.answer("💱")
        try:
            for token in coins_id_list:
                token_result = await get_price(token)
            await message.answer(token_result, reply_markup=ref_kb(token))
            logger.info(
            f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
            f"ID: {message.from_user.id} getting token data for '{message.text[1:]}'"
        )
        except:
            await message.answer(f"По запросу <b>{message.text}</b> ничего не найдено!", reply_markup=mm_kb())
            logger.info(
                f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
                f"ID: {message.from_user.id} getting FAIL data for '{message.text}'"
            )


@coingecko_router.callback_query(RefreshCoinFactory.filter(F.action == "refresh"))
async def callbacks_coin_refresher_fab(
        callback: types.CallbackQuery, 
        callback_data: CGSeachFactory) -> str:
    await coin_data_refresher(callback.message, callback_data)
    await callback.answer("Данные обновлены ☑️")


async def coin_data_refresher(message: types.Message, new_value: str):
    with suppress(TelegramBadRequest):
        val = getattr(new_value, 'value')
        result = await get_price(str(val))
        await message.edit_text(result, reply_markup=ref_kb(str(val)))
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} REFRESH '{val}' token"
    )


@coingecko_router.callback_query(CGSeachFactory.filter(F.action == "search"))
async def callbacks_cg_search_fab(
        callback: types.CallbackQuery, 
        callback_data: CGSeachFactory):
    await coingecko_seacher(callback.message, callback_data)


@coingecko_router.message(F.content_type.in_("text"))
async def cg_search_by_text(message: Message):
    """
    Usage example: search + [query]
    """
    await message.delete()
    await message.answer("🔎")
    result = await cg_searcher(str(message.text), 2)
    await message.answer(result, reply_markup=adv_search_kb(message.text))
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} searched (SHORT) '{message.text}' token"
    )


async def coingecko_seacher(message: types.Message, new_value: str):
    with suppress(TelegramBadRequest):
        val = getattr(new_value,'value')
        result = await cg_searcher(str(val), 1)
        await message.edit_text(result, reply_markup=bmm_kb())
    logger.info(
        f"USER: {message.from_user.full_name} USERNAME: {message.from_user.username} "
        f"ID: {message.from_user.id} viewed (LONG) '{val}' token"
    ) # TODO /user: CryptoApe instend of username/


# COINS INLINE MENU BUTTONS:
@coingecko_router.callback_query(CGTokenFactory.filter(F.action == "cgtoken"))
async def callbacks_cg_token_fab(query: CallbackQuery, callback_data: CGSeachFactory):
    val = getattr(callback_data, 'value')
    result = await get_price(str(val))
    await query.message.edit_text(result, reply_markup=ex_kb())
    logger.info(
        f"USER: {query.from_user.full_name} USERNAME: {query.from_user.username} "
        f"ID: {query.from_user.id} getting token data for '{val}'"
    )


# ECHO MESSAGE /must be last/
@coingecko_router.message()
async def echo(message: Message):
    """
    ECHO message
    """
    echo_text = (
        '<b>Команда не опознана!</b>\n'
        '<b>Используйте</b> /help'
    )
    await message.answer("❔")
    await message.answer(echo_text)
    logger.info(
        f"'ECHO' menu for USER: {message.from_user.full_name} "
        f"USERNAME: {message.from_user.username} ID: {message.from_user.id}"
    )