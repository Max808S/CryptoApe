import aiohttp
from utils.misc.logging import logger


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
                
                name = coin_data[0]['name']
                symbol = coin_data[0]['symbol'].upper()
                coin_cap_rank = coin_data[0]['market_cap_rank']

                current_price = coin_data[0]['current_price'] 
                market_cap = coin_data[0]['market_cap']
                total_volume = coin_data[0]['total_volume']
                high_24h = coin_data[0]['high_24h']
                low_24h = coin_data[0]['low_24h']
                ath = coin_data[0]['ath']
                percent_change_24h = coin_data[0]['price_change_percentage_24h_in_currency']
                percent_change_7d = coin_data[0]['price_change_percentage_7d_in_currency']
                percent_change_30d = coin_data[0]['price_change_percentage_30d_in_currency']
                # current_time = datetime.datetime.now().strftime('%H:%M:%S') # %m.%d # TODO # import datetime 
                
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
                none_text = '"⚠️" - информация отсутствует'

                coin_data_list = (
                    current_price,
                    market_cap,
                    total_volume,
                    high_24h,
                    low_24h,
                    ath,
                    percent_change_24h,
                    percent_change_7d,
                    percent_change_30d                   
                    )
                    
                if None in coin_data_list:
                    none_current_price = coin_data_list[0]
                    none_market_cap = coin_data_list[1]
                    none_total_volume = coin_data_list[2]
                    none_high_24h = coin_data_list[3]
                    none_low_24h = coin_data_list[4]
                    none_ath = coin_data_list[5]
                    none_percent_change_24h = coin_data_list[6]
                    none_percent_change_7d = coin_data_list[7]
                    none_percent_change_30d = coin_data_list[8]

                    logger.info(f"Getting NONE stats for {token}")

                    formatted_price = none_current_price if current_price == None else (("{0:,}".format(none_current_price).replace(",", " ")))
                    formatted_market_cap = none_market_cap if market_cap == None else (("{0:,}".format(none_market_cap).replace(",", " ")))
                    formatted_total_volume = none_total_volume if total_volume == None else (("{0:,}".format(none_total_volume).replace(",", " ")))
                    formatted_high_24h = none_high_24h if high_24h == None else (("{0:,}".format(none_high_24h).replace(",", " ")))
                    formatted_low_24h = none_low_24h if low_24h == None else (("{0:,}".format(none_low_24h).replace(",", " ")))
                    formatted_ath = none_ath if ath == None else (("{0:,}".format(none_ath).replace(",", " ")))
                    formatted_24h = none_percent_change_24h if percent_change_24h == None else float(("{:.1f}".format(none_percent_change_24h).replace(",", " ")))
                    formatted_7d = none_percent_change_7d if percent_change_7d == None else float(("{:.1f}".format(none_percent_change_7d).replace(",", " ")))
                    formatted_30d = none_percent_change_30d if percent_change_30d == None else float(("{:.1f}".format(none_percent_change_30d).replace(",", " ")))
                    
                    total_info = (
                        f'{name} - <b>{symbol}</b>  {rank_emoji} {coin_cap_rank}\n\n'
                        f'{current_price_emoji} <b>Текущая цена:</b> {formatted_price} <b>$</b>\n\n'
                        f'<b>Максимум и минимум за 24ч:</b>\n'
                        f'{high_24h_emoji} {formatted_high_24h} <b>$</b>  {low_24h_emoji} {formatted_low_24h} <b>$</b>\n'
                        f'{ath_emoji} <b>Максимум за всё время:</b> {formatted_ath} <b>$</b>\n\n'
                        f'{total_volume_emoji} <b>Объём за 24ч:</b> {formatted_total_volume} <b>$</b>\n'
                        f'{market_cap_emoji} <b>Капитализация:</b> {formatted_market_cap} <b>$</b>\n\n'
                        f'<b>Изменения цены в %:</b>\n'
                        f'{h24_emoji} <b>24ч:</b> {formatted_24h}%\n'
                        f'{d7_emoji} <b>7 дней:</b> {formatted_7d}%\n'
                        f'{d30_emoji} <b>30 дней:</b> {formatted_30d}%\n\n'
                        f'{none_text}'
                    )
                else:
                    logger.info(f"Getting FULL stats for {token}")
                    
                    # current price
                    high_price = '{0:,}'.format(current_price).replace(',', ' ')
                    low_price = '{:.8f}'.format(current_price)
                    formatted_current_price = (low_price if current_price < 0.0009 else high_price) # TODO
                    
                    coin_market_cap = '{0:,}'.format(market_cap).replace(',', ' ')
                    coin_volume = '{0:,}'.format(total_volume).replace(',', ' ')

                    # maximum and minimum price per 24h
                    high_price_high_24h = '{0:,}'.format(high_24h).replace(',', ' ')
                    high_price_low_24h = '{0:,}'.format(low_24h).replace(',', ' ')
                    low_price_high_24h = '{:.8f}'.format(high_24h)
                    low_price_low_24h = '{:.8f}'.format(low_24h)
                    formatted_high_24h = (low_price_high_24h if high_24h < 0.0009 else high_price_high_24h)
                    formatted_low_24h = (low_price_low_24h if low_24h < 0.0009 else high_price_low_24h)
                    
                    # ath
                    high_ath = '{0:,}'.format(ath).replace(',', ' ') 
                    low_ath = '{:.8f}'.format(ath)
                    formatted_ath = (low_ath if ath < 0.0009 else high_ath)

                    # percentage change in price
                    formatted_change_24h = float("{:.1f}".format(percent_change_24h))
                    formatted_change_7d = float("{:.1f}".format(percent_change_7d))
                    formatted_change_30d = float("{:.1f}".format(percent_change_30d))
                    
                    total_info = (
                        f'{name} - <b>{symbol}</b>  🏅 {coin_cap_rank}\n'
                        f'\n'
                        f'💵 <b>Текущая цена:</b> {formatted_current_price} <b>$</b>\n'
                        f'\n'
                        f'<b>Максимум и минимум за 24ч:</b>\n'
                        f'📈 {formatted_high_24h} <b>$</b>  📉 {formatted_low_24h} <b>$</b>\n'
                        f'<b>Максимум за всё время:</b> {formatted_ath} <b>$</b>\n\n'
                        f'📊 <b>Объём за 24ч:</b> {coin_volume} <b>$</b>\n'
                        f'📊 <b>Капитализация:</b> {coin_market_cap} <b>$</b>\n'
                        f'\n'
                        f'Изменения цены в %: \n'
                        f'{"📈" if percent_change_24h > 0 else "📉"} <b>24 ч:</b>  {formatted_change_24h}%\n'
                        f'{"📈" if percent_change_7d > 0 else "📉"} <b>7 дней:</b> {formatted_change_7d}%\n'
                        f'{"📈" if percent_change_30d > 0 else "📉"} <b>30 дней:</b> {formatted_change_30d}%\n'
                        )
            return total_info
    except Exception as ex:
        logger.info(f'Got an ERROR with the {token} token: \n{ex}')
        except_info = (
            f'Sorry, we got a problem with:\n'
            f'⚠️ {name} - <b>{symbol}</b>\n'
            f'Pls try /{token}\n'
            f'We already working on a fix'
        )
        return except_info


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
        ff_data = []

        for item in categories_data[:30]:
            coin_rank = item['market_cap_rank']
            coin_name = item['name']
            coin_symbol = item['symbol']
            coin_price = float("{:.2f}".format(item['current_price']))
            rank_emoji = "⚠️" if coin_rank == None else "🏅"
            gg_data.append(
                f'{coin_rank} {rank_emoji} /{coin_symbol} <b>{coin_name}</b> - {coin_price} $'
            )
            ff_data.append(
                f'/{coin_symbol} - {coin_price} $'
            )

        final_page_1 = ('\n'.join(gg_data))
        real_final = (
            f'Лучшие валюты в категории <b>«{category}»</b> по рыночной капитализации:\n\n'
            f'{final_page_1}'
            )
        
        final_page_2 = ('\n'.join(ff_data))
        real_final_2 = (
            f'Лучшие валюты в категории <b>«{category}»</b> по рыночной капитализации:\n\n'
            f'{final_page_2}'
            )

        return real_final_2
        # return real_final
    # except Exception as ex:
    #     logger.info(f'HUSTON WE HAVE A PROBLEM: \nCATEGORIES! \n{ex}')
        

