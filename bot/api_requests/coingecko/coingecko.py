import aiohttp
import datetime
# from datetime import datetime # TODO


async def get_price(token):
    async with aiohttp.ClientSession() as session:
        
        url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&'\
            'ids='+token+'&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=24h%2C7d%2C30d'
        
        coin_stats = {} # TODO
        async with session.get(url) as response:
            coin_data = await response.json()
            name = coin_data[0]["name"]
            symbol = coin_data[0]["symbol"]
            current_price = coin_data[0]["current_price"]
            coin_cap_rank = coin_data[0]['market_cap_rank']
            coin_ath = coin_data[0]['ath']
            coin_market_cap = coin_data[0]['market_cap']
            coin_volume = coin_data[0]['total_volume']
            coin_high_24h = coin_data[0]['high_24h']
            coin_low_24h = coin_data[0]['low_24h']

            ath_date = coin_data[0]['ath_date'] # TODO
            # iso_datetime = datetime.strftime(ath_date, "%Y-%m-%dT%H:%M:%S.%f%Z")
            # only_date = iso_datetime.date()
            
            percent_change_24h = float("{:.1f}".format(coin_data[0]['price_change_percentage_24h_in_currency']))
            percent_change_7d = float("{:.1f}".format(coin_data[0]['price_change_percentage_7d_in_currency']))
            percent_change_30d = float("{:.1f}".format(coin_data[0]['price_change_percentage_30d_in_currency']))
               
            current_time = datetime.datetime.now().strftime('%H:%M:%S')  # %m.%d
            total_info = (
                f'{name} - {symbol}  🏅 {coin_cap_rank}\n'
                f'\n'
                f'💵 Текущая цена: {current_price} $  - {current_time}\n'
                f'\n'
                f'Максимум и минимум за 24ч:\n'
                f'📈 {coin_high_24h} $  📉 {coin_low_24h} $\n'
                f'Максимум за всё время: {coin_ath} $\n\n'
                f'📊 Объём за 24ч: {coin_volume} $\n'
                f'📊 Капитализация: {coin_market_cap} $\n'
                f'\n'
                f'Изменения цены в %: \n'
                f'{"📈" if percent_change_24h > 0 else "📉"} 24 ч:  {percent_change_24h}%\n'
                f'{"📈" if percent_change_7d > 0 else "📉"} 7 дней: {percent_change_7d}%\n'
                f'{"📈" if percent_change_30d > 0 else "📉"} 30 дней: {percent_change_30d}%\n'
                )
        return total_info


# async def get_bitcoin_price():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd') as response:
#             bitcoin = await response.json()
#         return int(bitcoin["bitcoin"]["usd"])


# async def get_ethereum_price():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd') as response:
#             bitcoin = await response.json()
#         return bitcoin["swapall"]["usd"]