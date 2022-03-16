import aiohttp
import datetime
# from datetime import datetime # TODO
from utils.misc.logging import logger


async def get_cg_categories(category):
    """
    Getting cg categories
    """
    # try:
    async with aiohttp.ClientSession() as session:
        url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&'\
            'category='+str(category)+'&order=market_cap_desc&per_page=100&page=1&s'\
            'parkline=false&price_change_percentage=1h%2C24h%2C7d'
        
        async with session.get(url) as response:
            categories_data = await response.json()
            
        gg_data = []

        for item in categories_data[:30]:
            coin_rank = item['market_cap_rank']
            coin_name = item['name']
            coin_symbol = item['symbol']
            coin_price = float("{:.2f}".format(item['current_price']))
            rank_emoji = "⚠️" if coin_rank == None else "🏅"
            gg_data.append(
                f'{coin_rank} {rank_emoji} /{coin_symbol} <b>{coin_name}</b> - {coin_price} $'
            )
        
        final_page_1 = ('\n'.join(gg_data))
        real_final = (
            f'Лучшие валюты в категории <b>«{category}»</b> по рыночной капитализации:\n\n'
            f'{final_page_1}'
            )

        return real_final
    # except Exception as ex:
    #     logger.info(f'HUSTON WE HAVE A PROBLEM: \nCATEGORIES! \n{ex}')
        
async def get_price(token) -> str:
    """
    Getting token current price and another data
    """
    try:
        async with aiohttp.ClientSession() as session: 
            url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&'\
                'ids='+token+'&order=market_cap_desc&per_page=100&page=1&sparkline'\
                '=false&price_change_percentage=24h%2C7d%2C30d'
            
            async with session.get(url) as response:
                coin_data = await response.json()
                
                current_price = coin_data[0]['current_price'] 
                coin_data_list = (
                    coin_data[0]['current_price'],
                    coin_data[0]['market_cap'],
                    coin_data[0]['total_volume'],
                    coin_data[0]['high_24h'],
                    coin_data[0]['low_24h'],
                    coin_data[0]['ath'],
                    coin_data[0]['price_change_percentage_24h_in_currency'],
                    coin_data[0]['price_change_percentage_7d_in_currency'],
                    coin_data[0]['price_change_percentage_30d_in_currency']                   
                    )
                
                if None in coin_data_list:          
                    current_price = coin_data_list[0]
                    market_cap = coin_data_list[1]
                    total_volume = coin_data_list[2]
                    high_24h = coin_data_list[3]
                    low_24h = coin_data_list[4]
                    ath = coin_data_list[5]
                    percent_change_24h = coin_data_list[6]
                    percent_change_7d = coin_data_list[7]
                    percent_change_30d = coin_data_list[8]

                    logger.info(f"Getting NONE stats for {token}")
                    name = coin_data[0]['name']
                    symbol = coin_data[0]['symbol'].upper()
                    coin_cap_rank = coin_data[0]['market_cap_rank']
                    # current_time = datetime.datetime.now().strftime('%H:%M:%S')  # %m.%d

                    format_price = current_price if coin_data_list[0] == None else (("{0:,}".format(coin_data[0]["current_price"]).replace(",", " ")))
                    format_market_cap = market_cap if coin_data_list[1] == None else (("{0:,}".format(coin_data[0]["market_cap"]).replace(",", " ")))
                    format_total_volume = total_volume if coin_data_list[2] == None else (("{0:,}".format(coin_data[0]["total_volume"]).replace(",", " ")))
                    format_high_24h = high_24h if coin_data_list[3] == None else (("{0:,}".format(coin_data[0]["high_24h"]).replace(",", " ")))
                    format_low_24h = low_24h if coin_data_list[4] == None else (("{0:,}".format(coin_data[0]["low_24h"]).replace(",", " ")))
                    format_ath = ath if coin_data_list[5] == None else (("{0:,}".format(coin_data[0]["ath"]).replace(",", " ")))
                    format_24h = percent_change_24h if coin_data_list[6] == None else float(("{:.1f}".format(coin_data[0]["price_change_percentage_24h_in_currency"]).replace(",", " ")))
                    format_7d = percent_change_7d if coin_data_list[7] == None else float(("{:.1f}".format(coin_data[0]["price_change_percentage_7d_in_currency"]).replace(",", " ")))
                    format_30d = percent_change_30d if coin_data_list[8] == None else float(("{:.1f}".format(coin_data[0]["price_change_percentage_30d_in_currency"]).replace(",", " ")))
                    
                    rank_emoji = "⚠️" if coin_cap_rank == None else "🏅"
                    current_price_emoji = "⚠️" if current_price == None else "💵"
                    market_cap_emoji = "⚠️" if market_cap == None else "📊"
                    total_volume_emoji = "⚠️" if total_volume == None else "📊"
                    high_24h_emoji = "⚠️" if high_24h == None else "📈"
                    low_24h_emoji = "⚠️" if low_24h == None else "📉"
                    ath_emoji = "⚠️" if ath == None else "📈"
                    h24_emoji = "⚠️" if percent_change_24h == None else ("📈" if percent_change_24h > 0 else "📉")
                    d7_emoji = "⚠️" if percent_change_7d == None else ("📈" if percent_change_7d > 0 else "📉")
                    d30_emoji = "⚠️" if percent_change_30d == None else ("📈" if percent_change_30d > 0 else "📉")

                    total_info = (
                        f'{name} - <b>{symbol}</b>  {rank_emoji} {coin_cap_rank}\n\n'
                        f'{current_price_emoji} <b>Текущая цена:</b> {format_price} <b>$</b>\n\n'
                        f'<b>Максимум и минимум за 24ч:</b>\n'
                        f'{high_24h_emoji} {format_high_24h} <b>$</b>  {low_24h_emoji} {format_low_24h} <b>$</b>\n'
                        f'{ath_emoji} <b>Максимум за всё время:</b> {format_ath} <b>$</b>\n\n'
                        f'{total_volume_emoji} <b>Объём за 24ч:</b> {format_total_volume} <b>$</b>\n'
                        f'{market_cap_emoji} <b>Капитализация:</b> {format_market_cap} <b>$</b>\n\n'
                        f'<b>Изменения цены в %:</b>\n'
                        f'{h24_emoji} <b>24ч:</b> {format_24h}%\n'
                        f'{d7_emoji} <b>7 дней:</b> {format_7d}%\n'
                        f'{d30_emoji} <b>30 дней:</b> {format_30d}%'
                    )                    
                else:
                    logger.info(f"Getting FULL stats for {token}")
                    name = coin_data[0]["name"]
                    symbol = coin_data[0]["symbol"].upper()
                    
                    # current_price = '{0:,}'.format(coin_data[0]["current_price"]).replace(',', ' ')                    
                    # current_price = coin_data[0]['current_price']
                    
                    total_price = '{:.8f}'.format(current_price)
                    test_price = (total_price if current_price < 0.0009 else current_price) # TODO
                    
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
                        f'💵 <b>Текущая цена:</b> {test_price} <b>$</b>  - {current_time}\n'
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
        name = coin_data[0]["name"]
        symbol = coin_data[0]["symbol"].upper()
        except_info = (
            f'{name} - <b>{symbol}</b>'
        )
        return except_info