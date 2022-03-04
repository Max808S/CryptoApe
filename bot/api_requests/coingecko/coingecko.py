import aiohttp


async def get_bitcoin_price():
    # Делаем запрос на получение цены
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd') as response:
            bitcoin = await response.json()
        return int(bitcoin["bitcoin"]["usd"])


# async def get_ethereum_price():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
#                                      '&ids=bitcoin%2Cethereum%2Cbinancecoin%2Csolana%2Cpolkadot%2Cri'
#                                      'pple%2Ccardano%2Cterra-luna%2Cavalanche-2%2Cdogecoin%2Cmatic-n'
#                                      'etwork%2Cchainlink%2Cnear%2Clitecoin%2Ctron%2Cvechain%2Cstella'
#                                      'r%2Coasis-network%2Cgala%2Cthe-sandbox&order=id_asc&per_page=1'
#                                      '00&page=1&sparkline=false&price_change_percentage=24h%2C7d%2C3'
#                                      '0d%2C200d%2C1y') as response:
#             ethereum = await response.json()
#             coin_name = ethereum['name']
#             coin_price = ethereum['coin']['current_price']
#             coin_cap_rank = ethereum['coin']['market_cap_rank']
#             total = coin_name
#         return (total)




# class CoinInformation:
#     """
#     Functions with requests about coins
#     """

#     def get_coins_info(self, username, user_id) -> str:
#         try:
#             # counter = self
#             # coins_info = info_list[self]
#             coin_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
#                                      '&ids=bitcoin%2Cethereum%2Cbinancecoin%2Csolana%2Cpolkadot%2Cri'
#                                      'pple%2Ccardano%2Cterra-luna%2Cavalanche-2%2Cdogecoin%2Cmatic-n'
#                                      'etwork%2Cchainlink%2Cnear%2Clitecoin%2Ctron%2Cvechain%2Cstella'
#                                      'r%2Coasis-network%2Cgala%2Cthe-sandbox&order=id_asc&per_page=1'
#                                      '00&page=1&sparkline=false&price_change_percentage=24h%2C7d%2C3'
#                                      '0d%2C200d%2C1y').json()
#             coin_dump = json.dumps(coin_data)
#             coin_load = json.loads(coin_dump)
#             coin_name = coin_load[self]['name']
#             coin_price = coin_load[self]['current_price']
#             coin_cap_rank = coin_load[self]['market_cap_rank']
#             coin_ath = coin_load[self]['ath']
#             coin_market_cap = coin_load[self]['market_cap']
#             coin_volume = coin_load[self]['total_volume']
#             coin_high_24h = coin_load[self]['high_24h']
#             coin_low_24h = coin_load[self]['low_24h']
#             price_change_24h = coin_load[self]['price_change_percentage_24h_in_currency']
#             price_change_7d = coin_load[self]['price_change_percentage_7d_in_currency']
#             price_change_30d = coin_load[self]['price_change_percentage_30d_in_currency']
#             price_change_200d = coin_load[self]['price_change_percentage_200d_in_currency']
#             price_change_1y = coin_load[self]['price_change_percentage_1y_in_currency']
#             time = datetime.datetime.now().strftime('%H:%M:%S')  # %m.%d
#             total_info = f'{coins_info}' \
#                          f'\n ' \
#                          f'\n{coin_name} #{coin_cap_rank} в рейтинге капитализации' \
#                          f'\n ' \
#                          f'\nТекущая цена: {coin_price} $   {time}' \
#                          f'\n ' \
#                          f'\nМаксимум за всё время: {coin_ath} $' \
#                          f'\nМаксимум и минимум за 24ч:' \
#                          f'\n\U0001F4C8 {coin_high_24h} $  \U0001F4C9 {coin_low_24h} $' \
#                          f'\n\U0001F4CA Объём за 24ч: {coin_volume} $' \
#                          f'\n\U0001F4CA Капитализация: {coin_market_cap} $' \
#                          f'\n ' \
#                          f'\n\U000025AA 24ч:  {float("{:.1f}".format(price_change_24h))}%' \
#                          f'\n\U000025AA 7 дней:  {float("{:.1f}".format(price_change_7d))}%' \
#                          f'\n\U000025AA 30 дней:  {float("{:.1f}".format(price_change_30d))}%' \
#                          f'\n\U000025AA 200 дней:  {float("{:.1f}".format(price_change_200d))}%' \
#                          f'\n\U000025AA 1 год:  {float("{:.1f}".format(price_change_1y))}% '
#             # print(f'User {username} ID: {user_id} checked {coin_name}')
#             logging.info(f"Getting {coin_name} stats for {username} ID: {user_id}")
#             return total_info
#         except Exception as ex:
#             print(ex)









# ## TODO
# coin_names = {
# "eth": "ethereum",
# "btc": "bitcoin"
# }

# search_url = 'https://api.coingecko.com/api/v3/search?query='

# async def get_coin_price(coin_short_name: str) -> int:
#     coin_name = coin_names.get(coin_short_name)
#     if not coin_name:
#         return 0
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd') as response:
#             result = await response.json()
#         # return int(result[coin_name]["usd"])
#         print(int(result[coin_name]["usd"]))


# if __name__ == '__main__':
#     get_coin_price()







### TODO ###
# async def alarm(message: types.Message):
#     mean = int(input())
#     while True:
#         await asyncio.sleep(3)
#         if mean < await get_bitcoin_price():
#             await message.answer(f"Цена биткоина пересекла вашу отметку {mean}")
#             break
