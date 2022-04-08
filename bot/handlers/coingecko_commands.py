from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery

from api_requests.coingecko.coingecko import get_price, get_categories_data, get_trending_coins

from api_requests.coingecko.token_json import (
    dict_from_tokens_csv, cg_tokens_keys, cg_tokens_values,
    dict_from_cg_categories_csv, cg_categories_values,
    dict_with_token_ids, cg_token_extra_name
)

from keypads.keyboards import (
    get_extra_coins_keyboards as ex_kb,
    get_back_main_menu_keyboards as mm_kb,
    get_extra_categories_keyboards as ex_cat_kb,
    get_back_main_menu_keyboards as bmm_kb
)

from data.text_file import (
    trend_text, btc_text, eth_text, bnb_text, sol_text,
    ada_text, xrp_text, luna_text, dot_text, avax_text,
    doge_text, matic_text, link_text, near_text, ltc_text,
    trx_text, xlm_text, vet_text, sand_text, gala_text, oasis_text
)


coingecko_router = Router(name=__name__)


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
    await message.answer(full_res, reply_markup=mm_kb())


@coingecko_router.callback_query(F.data == "trend")
async def inline_trend_button(query: CallbackQuery) -> str:
    result = await get_trending_coins()
    full_res = (f'{trend_text}\n\n{result}')
    # await query.message.answer("🔎")
    await query.message.edit_text(full_res)
    await query.message.edit_reply_markup(reply_markup=bmm_kb())


# MENU CATEGORIES
@coingecko_router.message(commands=cg_categories_values)
async def cg_categories(message: types.Message) -> str:
    """
    Get categories
    """
    await message.delete()
    await message.answer("📂")
    for key, value in dict_from_cg_categories_csv.items():
        if value == message.text[1:]:
            result = await get_categories_data(key)
    await message.answer(result, reply_markup=ex_cat_kb())


# SEARCH TOKENS IN CSV BASE: token_name & token_id
@coingecko_router.message(commands=cg_tokens_keys)
async def token_name(message: types.Message) -> str:
    """
    Checking the coin in the database (CSV COINS LIST) by name.
    Usage example: /tron-bsc /wrapped-tron
    """
    await message.answer("💱")
    await message.delete()
    result = await get_price(message.text[1:])
    await message.answer(result, reply_markup=mm_kb())


@coingecko_router.message(commands=cg_token_extra_name)
async def token_extra_id(message: types.Message) -> str:
    """
    Checking the coin in the database (CSV COINS LIST) by extra id.
    Example: /tron_bsc /wrapped_tron, bitcoin, solana   /USED: "_"/
    """
    await message.answer("💱")
    await message.delete()
    for key, value in dict_with_token_ids.items():
        if value == message.text[1:]:
            result = await get_price(key)
    await message.answer(result, reply_markup=mm_kb())


@coingecko_router.message(commands=cg_tokens_values)
async def token_id(message: types.Message) -> str:
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
        listToStr = '\n/'.join([str(elem).replace("-", "_") for elem in coins_id_list])
        result = f"Pick your coin:\n/{listToStr}"
        await message.answer(result, reply_markup=mm_kb)
    else:
        await message.answer("💱")
        for token in coins_id_list:
            token_result = await get_price(token)
        await message.answer(token_result, reply_markup=mm_kb())


# (TEXT) SEARCH TOKENS IN CSV BASE: token_name & token_id
@coingecko_router.message(F.text.in_(cg_tokens_values))
async def text_token_id(message: types.Message) -> str:
    """
    Usage example: bnb, sol, trx    # TODO create list for
    """
    await message.delete()
    await message.answer("💱")
    for key, value in dict_from_tokens_csv.items():
        if value == message.text:
            result = await get_price(key)
    await message.answer(result, reply_markup=mm_kb())


@coingecko_router.message(F.text.in_(cg_tokens_keys))
async def text_token_name(message: types.Message) -> str:
    """
    Usage example: tron-bsc, wrapped-tron
    """
    await message.delete()
    await message.answer("💱")
    result = await get_price(message.text)
    await message.answer(result, reply_markup=mm_kb())


@coingecko_router.message(F.text.in_(cg_token_extra_name))
async def text_token_extra_name(message: types.Message) -> str:
    """
    Usage example: tron_bsc, bitcoin, binancecoin
    """
    await message.delete()
    await message.answer("💱")
    for key, value in dict_with_token_ids.items():
        if value == message.text:
            result = await get_price(key)
    await message.answer(result, reply_markup=mm_kb())


# COINS MENU INLINE BUTTONS
@coingecko_router.callback_query(F.data == "btc")
async def btc_button(query: CallbackQuery) -> str:
    result = await get_price("bitcoin")
    final_result = f'<tg-spoiler>{btc_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "eth")
async def eth_button(query: CallbackQuery) -> str:
    result = await get_price("ethereum")
    final_result = f'<tg-spoiler>{eth_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "bnb")
async def bnb_button(query: CallbackQuery) -> str:
    result = await get_price("binancecoin")
    final_result = f'<tg-spoiler>{bnb_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "sol")
async def sol_button(query: CallbackQuery) -> str:
    result = await get_price("solana")
    final_result = f'<tg-spoiler>{sol_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "dot")
async def dot_button(query: CallbackQuery) -> str:
    result = await get_price("polkadot")
    final_result = f'<tg-spoiler>{dot_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "xrp")
async def xrp_button(query: CallbackQuery) -> str:
    result = await get_price("ripple")
    final_result = f'<tg-spoiler>{xrp_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "ada")
async def ada_button(query: CallbackQuery) -> str:
    result = await get_price("cardano")
    final_result = f'<tg-spoiler>{ada_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "luna")
async def luna_button(query: CallbackQuery) -> str:
    result = await get_price("terra-luna")
    final_result = f'<tg-spoiler>{luna_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "avax")
async def avax_button(query: CallbackQuery) -> str:
    result = await get_price("avalanche-2")
    final_result = f'<tg-spoiler>{avax_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "doge")
async def doge_button(query: CallbackQuery) -> str:
    result = await get_price("dogecoin")
    final_result = f'<tg-spoiler>{doge_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "matic")
async def matic_button(query: CallbackQuery) -> str:
    result = await get_price("matic-network")
    final_result = f'<tg-spoiler>{matic_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "link")
async def link_button(query: CallbackQuery) -> str:
    result = await get_price("chainlink")
    final_result = f'<tg-spoiler>{link_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "near")
async def near_button(query: CallbackQuery) -> str:
    result = await get_price("near")
    final_result = f'<tg-spoiler>{near_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "ltc")
async def ltc_button(query: CallbackQuery) -> str:
    result = await get_price("litecoin")
    final_result = f'<tg-spoiler>{ltc_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "trx")
async def trx_button(query: CallbackQuery) -> str:
    result = await get_price("tron")
    final_result = f'<tg-spoiler>{trx_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "xlm")
async def xlm_button(query: CallbackQuery) -> str:
    result = await get_price("stellar")
    final_result = f'<tg-spoiler>{xlm_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "vet")
async def vet_button(query: CallbackQuery) -> str:
    result = await get_price("vechain")
    final_result = f'<tg-spoiler>{vet_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "sand")
async def sand_button(query: CallbackQuery) -> str:
    result = await get_price("the-sandbox")
    final_result = f'<tg-spoiler>{sand_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "gala")
async def gala_button(query: CallbackQuery) -> str:
    result = await get_price("gala")
    final_result = f'<tg-spoiler>{gala_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


@coingecko_router.callback_query(F.data == "oasis")
async def oasis_button(query: CallbackQuery) -> str:
    result = await get_price("oasis-network")
    final_result = f'<tg-spoiler>{oasis_text}</tg-spoiler>\n\n{result}'
    await query.message.edit_text(final_result)
    await query.message.edit_reply_markup(reply_markup=ex_kb())


# ECHO MESSAGE /must be last/
@coingecko_router.message()
async def echo(message: Message) -> str:
    """
    ECHO message
    """
    echo_text = (
        '<b>Команда не опознана!</b>\n'
        'Ваше сообщение:\n'
        f'{message.text}\n\n'
        '<b>Используйте</b> /help'
    )
    await message.answer("❔")
    await message.answer(echo_text)