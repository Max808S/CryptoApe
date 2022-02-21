import aiohttp


async def get_bitcoin_price():
    # Делаем запрос на получение цены
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd') as response:
            bitcoin = await response.json()
        return int(bitcoin["bitcoin"]["usd"])


async def get_ethereum_price():
    # Делаем запрос на получение цены
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd') as response:
            ethereum = await response.json()
        return int(ethereum["ethereum"]["usd"])


# ## TODO
# coin_names = {
# "eth": "ethereum",
# "btc": "bitcoin"
# }

# async def get_coin_price(coin_short_name: str) -> int:
#     coin_name = coin_names.get(coin_short_name)
#     if not coin_name:
#         return 0
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd') as response:
#             result = await response.json()
#         return int(result[coin_name]["usd"])



# search_url = 'https://api.coingecko.com/api/v3/search?query='

# async def search_coingecko():
#     async with aiohttp.ClientSession() as session:
#         async with session.get()






### TODO ###
# async def alarm(message: types.Message):
#     mean = int(input())
#     while True:
#         await asyncio.sleep(3)
#         if mean < await get_bitcoin_price():
#             await message.answer(f"Цена биткоина пересекла вашу отметку {mean}")
#             break
