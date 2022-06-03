from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from contextlib import suppress
from misc.logging import logger
from misc.text_file import trend_text

from api_requests.coingecko.coingecko import (
    get_price, get_categories_data, get_trending_coins,
    cg_searcher, get_tokens_stat
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
    get_market_cap_stats_menu_keyboards as mc_kb,
    get_extra_market_cap_stats_menu_keyboards as ex_mc_kb,
    get_volume_stats_menu_keyboards as vol_kb,
    get_extra_volume_stats_menu_keyboards as ex_vol_kb,
    get_1h_tokens_stat_menu_keyboards as h1_kb,
    get_extra_1h_tokens_stat_menu_keyboards as ex_h1_kb,
    get_24h_tokens_stat_menu_keyboards as h24_kb,
    get_extra_24h_tokens_stat_menu_keyboards as ex_h24_kb,
    get_7d_tokens_stat_menu_keyboards as d7_kb,
    get_extra_7d_tokens_stat_menu_keyboards as ex_d7_kb,
    CGSeachFactory, RefreshCoinFactory, CGTokenFactory,
    CoinRateFactory, MarketCapFactory, TotalVolumeFactory,
    H1_Factory, H24_Factory, D7_Factory
)


coingecko_router = Router(name=__name__)


# RANKING TOKENS:
@coingecko_router.message(commands="ranking")
async def get_tokens_view(message: types.Message) -> str:
    """
    [COMMAND] Get coins stats.
    """
    await message.delete()
    result = await get_tokens_stat("market_cap_desc", "market_cap", 1)
    await message.answer(result, reply_markup=mc_kb(), disable_web_page_preview=True)
    logger.info(
        f"USER: {message.from_user.full_name} @{message.from_user.username} "
        f"ID: {message.from_user.id} getting 'TOKENS VIEW' menu"
    )


@coingecko_router.callback_query(F.data == "ranking")
async def inline_tokens_view_button(query: CallbackQuery):
    """
    [BUTTON] Get coins stats. 
    """
    result = await get_tokens_stat("market_cap_desc", "market_cap", 1) # TODO
    await query.message.edit_text(result, reply_markup=mc_kb())
    logger.info(
        f"USER: {query.from_user.full_name} @{query.from_user.username} "
        f"ID: {query.from_user.id} getting 'RANK' inline menu"
    )


# Market Cap / Total Volume / Percentage (1h, 24h, 7d)
@coingecko_router.callback_query(CoinRateFactory.filter(F.action == "cgrate"))
async def callbacks_coins_stat_fab(query: CallbackQuery, callback_data: CGSeachFactory):
    val = getattr(callback_data, 'value')
    try:
        if val == "market_cap_desc":
            result = await get_tokens_stat(val, "market_cap", 1)
            await query.message.edit_text(result, reply_markup=mc_kb())
        elif val == "volume_desc":
            result = await get_tokens_stat(val, "total_volume", 1)
            await query.message.edit_text(result, reply_markup=vol_kb())
        elif val == "h1_result":
            result = await get_tokens_stat("market_cap_desc", "h1_result", 1)
            await query.message.edit_text(result, reply_markup=h1_kb())
        elif val == "h24_result":
            result = await get_tokens_stat("market_cap_desc", "h24_result", 1)
            await query.message.edit_text(result, reply_markup=h24_kb())
        elif val == "d7_result":
            result = await get_tokens_stat("market_cap_desc", "d7_result", 1)
            await query.message.edit_text(result, reply_markup=d7_kb())
    except TelegramBadRequest:
        await query.answer(f"Обновлено ☑️")
    logger.info(
        f"USER: {query.from_user.full_name} @{query.from_user.username} "
        f"ID: {query.from_user.id} getting '{val}' stat."
    )


# Market Cap [PAGES]
@coingecko_router.callback_query(MarketCapFactory.filter(F.action == "market_cap_page"))
async def callbacks_market_cap_fab(query: CallbackQuery, callback_data: CGSeachFactory):
    val = getattr(callback_data, 'value')
    result = await get_tokens_stat("market_cap_desc", "market_cap", val)
    try:
        if val <= 5:
            await query.message.edit_text(result, reply_markup=mc_kb())
            await query.answer(f"#{val} ☑️")
        else:
            await query.message.edit_text(result, reply_markup=ex_mc_kb())
            await query.answer(f"#{val} ☑️")
    except TelegramBadRequest:
        await query.answer(f"#{val} ☑️")
    logger.info(
        f"USER: {query.from_user.full_name} @{query.from_user.username} "
        f"ID: {query.from_user.id} getting MARKET CAP PAGE '{val}' stat."
    )


# Total Volume [PAGES]
@coingecko_router.callback_query(TotalVolumeFactory.filter(F.action == "volume_page"))
async def callbacks_total_vol_fab(query: CallbackQuery, callback_data: CGSeachFactory):
    val = getattr(callback_data, 'value')
    result = await get_tokens_stat("volume_desc", "total_volume", val)
    try:
        if val <= 5:
            await query.message.edit_text(result, reply_markup=vol_kb())
            await query.answer(f"#{val} ☑️")
        else:
            await query.message.edit_text(result, reply_markup=ex_vol_kb())
            await query.answer(f"#{val} ☑️")
    except TelegramBadRequest:
        await query.answer(f"#{val} ☑️")
    logger.info(
        f"USER: {query.from_user.full_name} @{query.from_user.username} "
        f"ID: {query.from_user.id} getting TOTAL VOLUME PAGE '{val}' stat."
    )


# 1h [PAGES]
@coingecko_router.callback_query(H1_Factory.filter(F.action == "h1_list"))
async def callbacks_1h_stat_fab(query: CallbackQuery, callback_data: CGSeachFactory):
    val = getattr(callback_data, 'value')
    result = await get_tokens_stat("market_cap_desc", "h1_result", val)
    try:
        if val <= 5:
            await query.message.edit_text(result, reply_markup=h1_kb())
            await query.answer(f"#{val} ☑️")
        else:
            await query.message.edit_text(result, reply_markup=ex_h1_kb())
            await query.answer(f"#{val} ☑️")
    except TelegramBadRequest:
        await query.answer(f"#{val} ☑️")
    logger.info(
        f"USER: {query.from_user.full_name} @{query.from_user.username} "
        f"ID: {query.from_user.id} getting 1 HOUR stat PAGE '{val}'."
    )


# 24h [PAGES]
@coingecko_router.callback_query(H24_Factory.filter(F.action == "h24_list"))
async def callbacks_24h_stat_fab(query: CallbackQuery, callback_data: CGSeachFactory):
    val = getattr(callback_data, 'value')
    result = await get_tokens_stat("market_cap_desc", "h24_result", val)
    try:
        if val <= 5:
            await query.message.edit_text(result, reply_markup=h24_kb())
            await query.answer(f"#{val} ☑️")
        else:
            await query.message.edit_text(result, reply_markup=ex_h24_kb())
            await query.answer(f"#{val} ☑️")
    except TelegramBadRequest:
        await query.answer(f"#{val} ☑️")
    logger.info(
        f"USER: {query.from_user.full_name} @{query.from_user.username} "
        f"ID: {query.from_user.id} getting 24 HOURs stat PAGE '{val}'."
    )


# 7d [PAGES]
@coingecko_router.callback_query(D7_Factory.filter(F.action == "d7_list"))
async def callbacks_7d_stat_fab(query: CallbackQuery, callback_data: CGSeachFactory):
    val = getattr(callback_data, 'value')
    result = await get_tokens_stat("market_cap_desc", "d7_result", val)
    try:
        if val <= 5:
            await query.message.edit_text(result, reply_markup=d7_kb())
            await query.answer(f"#{val} ☑️")
        else:
            await query.message.edit_text(result, reply_markup=ex_d7_kb())
            await query.answer(f"#{val} ☑️")
    except TelegramBadRequest:
        await query.answer(f"#{val} ☑️")
    logger.info(
        f"USER: {query.from_user.full_name} @{query.from_user.username} "
        f"ID: {query.from_user.id} getting 7 DAYs stat PAGE '{val}'."
    )


# TRENDING COINS:
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
        f"USER: {message.from_user.full_name} @{message.from_user.username} "
        f"ID: {message.from_user.id} getting 'TREND' menu"
    )


@coingecko_router.callback_query(F.data == "trend")
async def inline_trend_button(query: CallbackQuery):
    result = await get_trending_coins()
    full_res = (f'{trend_text}\n\n{result}')
    await query.message.edit_text(full_res, reply_markup=bmm_kb(), disable_web_page_preview=True)
    logger.info(
        f"USER: {query.from_user.full_name} @{query.from_user.username} "
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
        f"USER: {message.from_user.full_name} @{message.from_user.username} "
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
        f"USER: {message.from_user.full_name} @{message.from_user.username} "
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
        f"USER: {message.from_user.full_name} @{message.from_user.username} "
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
            f"USER: {message.from_user.full_name} @{message.from_user.username} "
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
                f"USER: {message.from_user.full_name} @{message.from_user.username} "
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
        f"USER: {message.from_user.full_name} @{message.from_user.username} "
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
        f"USER: {message.from_user.full_name} @{message.from_user.username} "
        f"ID: {message.from_user.id} searched (SHORT) '{message.text}' token"
    )


async def coingecko_seacher(message: types.Message, new_value: str):
    with suppress(TelegramBadRequest):
        val = getattr(new_value,'value')
        result = await cg_searcher(str(val), 1)
        await message.edit_text(result, reply_markup=bmm_kb())
    logger.info(
        f"USER: {message.from_user.full_name} @{message.from_user.username} "
        f"ID: {message.from_user.id} viewed (LONG) '{val}' token"
    ) # TODO /user: CryptoApe instend of username/


# COINS INLINE MENU BUTTONS:
@coingecko_router.callback_query(CGTokenFactory.filter(F.action == "cgtoken"))
async def callbacks_cg_token_fab(query: CallbackQuery, callback_data: CGSeachFactory):
    val = getattr(callback_data, 'value')
    result = await get_price(str(val))
    await query.message.edit_text(result, reply_markup=ex_kb())
    logger.info(
        f"USER: {query.from_user.full_name} @{query.from_user.username} "
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
        f"@{message.from_user.username} ID: {message.from_user.id}"
    )