import aiohttp
import datetime
# from datetime import datetime # TODO
from utils.misc.logging import logger


async def get_price(token):
    """
    Getting token current price and another data
    """
    try:
        async with aiohttp.ClientSession() as session: 
            url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&'\
                'ids='+token+'&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=24h%2C7d%2C30d'
            
            async with session.get(url) as response:
                coin_data = await response.json()
                none_list = (coin_data[0]['price_change_percentage_30d_in_currency'], coin_data[0]['price_change_percentage_7d_in_currency'], coin_data[0]['price_change_percentage_24h_in_currency'])
                if none_list[0] == None:    # TODO
                    logger.info(f"Getting LOW stats for {token}")
                    name = coin_data[0]["name"]
                    symbol = coin_data[0]["symbol"].upper()
                    current_price = '{0:,}'.format(coin_data[0]["current_price"]).replace(',', ' ')
                    coin_cap_rank = coin_data[0]['market_cap_rank']
                    coin_ath = coin_data[0]['ath']
                    coin_market_cap = '{0:,}'.format(coin_data[0]['market_cap']).replace(',', ' ')
                    coin_volume = '{0:,}'.format(coin_data[0]['total_volume']).replace(',', ' ')
                    coin_high_24h = '{0:,}'.format(coin_data[0]['high_24h']).replace(',', ' ')
                    coin_low_24h = '{0:,}'.format(coin_data[0]['low_24h']).replace(',', ' ')
                    current_time = datetime.datetime.now().strftime('%H:%M:%S')  # %m.%d
                    percent_change_24h = float("{:.1f}".format(coin_data[0]['price_change_percentage_24h_in_currency']))
                    percent_change_7d = float("{:.1f}".format(coin_data[0]['price_change_percentage_7d_in_currency']))
                    # percent_change_30d = float("{:.1f}".format(coin_data[0]['price_change_percentage_30d_in_currency']))
                    total_info = (
                        f'{name} - <b>{symbol}</b>  🏅 {coin_cap_rank}\n'
                        f'\n'
                        f'💵 <b>Текущая цена:</b> {current_price} <b>$</b>  - {current_time}\n'
                        f'\n'
                        f'<b>Максимум и минимум за 24ч:</b>\n'
                        f'📈 {coin_high_24h} $  📉 {coin_low_24h} $\n'
                        f'<b>Максимум за всё время:</b> {coin_ath} $\n\n'
                        f'📊 <b>Объём за 24ч:</b> {coin_volume} $\n'
                        f'📊 <b>Капитализация:</b> {coin_market_cap} $\n'
                        f'\n'
                        f'Изменения цены в %: \n'
                        f'{"📈" if percent_change_24h > 0 else "📉"} <b>24 ч:</b>  {percent_change_24h}%\n'
                        f'{"📈" if percent_change_7d > 0 else "📉"} <b>7 дней:</b> {percent_change_7d}%\n'
                        # f'{"📈" if percent_change_30d > 0 else "📉"} <b>30 дней:</b> {percent_change_30d}%\n'                     
                        )
                else:
                    logger.info(f"Getting FULL stats for {token}")
                    name = coin_data[0]["name"]
                    symbol = coin_data[0]["symbol"].upper()
                    current_price = '{0:,}'.format(coin_data[0]["current_price"]).replace(',', ' ')
                    coin_cap_rank = coin_data[0]['market_cap_rank']
                    coin_ath = coin_data[0]['ath']
                    coin_market_cap = '{0:,}'.format(coin_data[0]['market_cap']).replace(',', ' ')
                    coin_volume = '{0:,}'.format(coin_data[0]['total_volume']).replace(',', ' ')
                    coin_high_24h = '{0:,}'.format(coin_data[0]['high_24h']).replace(',', ' ')
                    coin_low_24h = '{0:,}'.format(coin_data[0]['low_24h']).replace(',', ' ')
                    
                    percent_change_24h = float("{:.1f}".format(coin_data[0]['price_change_percentage_24h_in_currency']))
                    percent_change_7d = float("{:.1f}".format(coin_data[0]['price_change_percentage_7d_in_currency']))
                    percent_change_30d = float("{:.1f}".format(coin_data[0]['price_change_percentage_30d_in_currency']))
                    
                    current_time = datetime.datetime.now().strftime('%H:%M:%S')  # %m.%d
                    total_info = (
                        f'{name} - <b>{symbol}</b>  🏅 {coin_cap_rank}\n'
                        f'\n'
                        f'💵 <b>Текущая цена:</b> {current_price} <b>$</b>  - {current_time}\n'
                        f'\n'
                        f'<b>Максимум и минимум за 24ч:</b>\n'
                        f'📈 {coin_high_24h} $  📉 {coin_low_24h} $\n'
                        f'<b>Максимум за всё время:</b> {coin_ath} $\n\n'
                        f'📊 <b>Объём за 24ч:</b> {coin_volume} $\n'
                        f'📊 <b>Капитализация:</b> {coin_market_cap} $\n'
                        f'\n'
                        f'Изменения цены в %: \n'
                        f'{"📈" if percent_change_24h > 0 else "📉"} <b>24 ч:</b>  {percent_change_24h}%\n'
                        f'{"📈" if percent_change_7d > 0 else "📉"} <b>7 дней:</b> {percent_change_7d}%\n'
                        f'{"📈" if percent_change_30d > 0 else "📉"} <b>30 дней:</b> {percent_change_30d}%\n'
                        )
            return total_info
    except Exception as ex:
        logger.info(f'HUSTON WE HAVE A PROBLEM: \ncoingecko > get_price: {ex}')
        return 'PLS try again later...'


### previous working function ###
# async def get_price(token):
#     """
#     Getting token current price and another data
#     """
#     logger.info(f"Getting coin stats for {token}")
#     async with aiohttp.ClientSession() as session:
#         try:    
#             url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&'\
#                 'ids='+token+'&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=24h%2C7d%2C30d'
            
#             coin_stats = {} # TODO
#             async with session.get(url) as response:
#                 coin_data = await response.json()
#                 name = coin_data[0]["name"]
#                 symbol = coin_data[0]["symbol"].upper()
#                 current_price = '{0:,}'.format(coin_data[0]["current_price"]).replace(',', ' ')
#                 coin_cap_rank = coin_data[0]['market_cap_rank']
#                 coin_ath = coin_data[0]['ath']
#                 coin_market_cap = '{0:,}'.format(coin_data[0]['market_cap']).replace(',', ' ')
#                 coin_volume = '{0:,}'.format(coin_data[0]['total_volume']).replace(',', ' ')
#                 coin_high_24h = '{0:,}'.format(coin_data[0]['high_24h']).replace(',', ' ')
#                 coin_low_24h = '{0:,}'.format(coin_data[0]['low_24h']).replace(',', ' ')

#                 ath_date = coin_data[0]['ath_date'] # TODO
#                 # iso_datetime = datetime.strftime(ath_date, "%Y-%m-%dT%H:%M:%S.%f%Z")
#                 # only_date = iso_datetime.date()
                
#                 percent_change_24h = float("{:.1f}".format(coin_data[0]['price_change_percentage_24h_in_currency']))
#                 percent_change_7d = float("{:.1f}".format(coin_data[0]['price_change_percentage_7d_in_currency']))
#                 percent_change_30d = float("{:.1f}".format(coin_data[0]['price_change_percentage_30d_in_currency']))
                
#                 current_time = datetime.datetime.now().strftime('%H:%M:%S')  # %m.%d
#                 total_info = (
#                     f'{name} - <b>{symbol}</b>  🏅 {coin_cap_rank}\n'
#                     f'\n'
#                     f'💵 <b>Текущая цена:</b> {current_price} <b>$</b>  - {current_time}\n'
#                     f'\n'
#                     f'<b>Максимум и минимум за 24ч:</b>\n'
#                     f'📈 {coin_high_24h} $  📉 {coin_low_24h} $\n'
#                     f'<b>Максимум за всё время:</b> {coin_ath} $\n\n'
#                     f'📊 <b>Объём за 24ч:</b> {coin_volume} $\n'
#                     f'📊 <b>Капитализация:</b> {coin_market_cap} $\n'
#                     f'\n'
#                     f'Изменения цены в %: \n'
#                     f'{"📈" if percent_change_24h > 0 else "📉"} <b>24 ч:</b>  {percent_change_24h}%\n'
#                     f'{"📈" if percent_change_7d > 0 else "📉"} <b>7 дней:</b> {percent_change_7d}%\n'
#                     f'{"📈" if percent_change_30d > 0 else "📉"} <b>30 дней:</b> {percent_change_30d}%\n'
#                     )
#         except Exception as ex:
#             logger.info(
#                 f"{token} not found percentage. Checking without percantage.."
#                 )
#             url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&'\
#                 'ids='+token+'&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=24h%2C7d%2C30d'
            
#             coin_stats = {} # TODO
#             async with session.get(url) as response:
#                 coin_data = await response.json()
#                 name = coin_data[0]["name"]
#                 symbol = coin_data[0]["symbol"]
#                 current_price = coin_data[0]["current_price"]
#                 coin_cap_rank = coin_data[0]['market_cap_rank']
#                 coin_ath = coin_data[0]['ath']
#                 coin_market_cap = coin_data[0]['market_cap']
#                 coin_volume = coin_data[0]['total_volume']
#                 coin_high_24h = coin_data[0]['high_24h']
#                 coin_low_24h = coin_data[0]['low_24h']

#                 ath_date = coin_data[0]['ath_date'] # TODO
#                 # iso_datetime = datetime.strftime(ath_date, "%Y-%m-%dT%H:%M:%S.%f%Z")
#                 # only_date = iso_datetime.date()
                
#                 current_time = datetime.datetime.now().strftime('%H:%M:%S')  # %m.%d
#                 total_info = (
#                     f'{name} - {symbol}  🏅 {coin_cap_rank}\n'
#                     f'\n'
#                     f'💵 Текущая цена: {current_price} $  - {current_time}\n'
#                     f'\n'
#                     f'Максимум и минимум за 24ч:\n'
#                     f'📈 {coin_high_24h} $  📉 {coin_low_24h} $\n'
#                     f'Максимум за всё время: {coin_ath} $\n\n'
#                     f'📊 Объём за 24ч: {coin_volume} $\n'
#                     f'📊 Капитализация: {coin_market_cap} $\n'
#                     )
#         return total_info


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