import aiohttp


async def get_price(token: str) -> str:
    """
    Getting token current price and another data
    """
    async with aiohttp.ClientSession() as session: 
        url = (
            "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&"
            "ids="+token+"&order=market_cap_desc&per_page=100&page=1&sparkline"
            "=false&price_change_percentage=24h%2C7d%2C30d"
        )

        async with session.get(url) as response:
            coin_data = await response.json()
            
            name = coin_data[0]["name"]
            symbol = coin_data[0]["symbol"].upper()
            coin_cap_rank = coin_data[0]["market_cap_rank"]
            current_price = coin_data[0]["current_price"] 
            market_cap = coin_data[0]["market_cap"]
            total_volume = coin_data[0]["total_volume"]
            high_24h = coin_data[0]["high_24h"]
            low_24h = coin_data[0]["low_24h"]
            ath = coin_data[0]["ath"]
            ath_date = coin_data[0]["ath_date"]
            percent_change_24h = coin_data[0]["price_change_percentage_24h_in_currency"]
            percent_change_7d = coin_data[0]["price_change_percentage_7d_in_currency"]
            percent_change_30d = coin_data[0]["price_change_percentage_30d_in_currency"]
            
            formatted_coin_rank = "❓" if coin_cap_rank == None else coin_cap_rank
            h24_emoji = "⚠️" if percent_change_24h == None else ("📈" if percent_change_24h > 0 else "📉")
            d7_emoji = "⚠️" if percent_change_7d == None else ("📈" if percent_change_7d > 0 else "📉")
            d30_emoji = "⚠️" if percent_change_30d == None else ("📈" if percent_change_30d > 0 else "📉")
            
            # current price
            formatted_current_price = "❓" if current_price == None else (
                ("{:.8f}".format(current_price)) if current_price < 0.0009 else (
                    "{0:,}".format(current_price).replace(",", " ")
                )
            )
            
            # token stats
            formatted_market_cap = "❓" if market_cap == None else (
                "❓" if market_cap == 0 else ("{0:,}".format(market_cap).replace(",", " "))
            )
            formatted_volume = "❓" if total_volume == None else (
                "❓" if total_volume == 0 else ("{0:,}".format(total_volume).replace(",", " "))
            )

            # maximum and minimum price per 24h
            formatted_high_24h = "❓" if high_24h == None else (
                ("{:.8f}".format(high_24h)) if high_24h < 0.0009 else ("{0:,}".format(high_24h).replace(",", " "))
            )
            formatted_low_24h = "❓" if low_24h == None else (
                ("{:.8f}".format(low_24h)) if low_24h < 0.0009 else ("{0:,}".format(low_24h).replace(",", " "))
            )
            
            # ath
            formatted_ath = "❓" if ath == None else (
                ("{:.8f}".format(ath)) if ath < 0.0009 else ("{0:,}".format(ath).replace(",", " "))
            )
            formatted_ath_date = "❓" if ath_date == None else ath_date.replace("T"," ").split(" ")[0]
            
            # percentage change in price
            formatted_change_24h = "❓" if percent_change_24h == None else float("{:.1f}".format(percent_change_24h))
            formatted_change_7d = "❓" if percent_change_7d == None else float("{:.1f}".format(percent_change_7d))
            formatted_change_30d = "❓" if percent_change_30d == None else float("{:.1f}".format(percent_change_30d))
            
            total_info = (
                f"{name} - <b>{symbol}</b>  🏅 - {formatted_coin_rank}\n\n"
                f"💵 <b>Текущая цена:</b> {formatted_current_price} <b>$</b>\n\n"
                f"<b>Максимум и минимум за 24ч:</b>\n"
                f"📈 {formatted_high_24h} <b>$</b>  📉 {formatted_low_24h} <b>$</b>\n"
                f"<b>Исторический максимум:</b> "
                f"\n📈 {formatted_ath} <b>$</b> - {formatted_ath_date}\n\n"
                f"📊 <b>Капитализация:</b> \n{formatted_market_cap} <b>$</b>\n"
                f"📊 <b>Объём за 24ч:</b> \n{formatted_volume} <b>$</b>\n\n"
                f"Изменения цены в %:\n"
                f"{h24_emoji} <b>24 ч:</b>  {formatted_change_24h}%\n"
                f"{d7_emoji} <b>7 дней:</b> {formatted_change_7d}%\n"
                f"{d30_emoji} <b>30 дней:</b> {formatted_change_30d}%\n"
                )
    return total_info


async def cg_searcher(query: str, mode: int) -> str:
    """
    Search for coins, categories and markets listed on CoinGecko ordered by largest Market Cap first
    """
    async with aiohttp.ClientSession() as session:
        url = "https://api.coingecko.com/api/v3/search?query="+query
        
        async with session.get(url) as response:
            response_data = await response.json()
        
        coins_list = []
        categories_list = []
        exchanges_list = []

        if mode == 1: # full
            for coin in response_data["coins"]:
                token_id = coin["id"]
                token_name = coin["name"]
                token_symbol = coin["symbol"]
                token_rank = coin["market_cap_rank"]
                coins_list.append(
                    f"{'❓' if token_rank == None else token_rank} 🏅  <b>{token_symbol.upper()}</b> - {token_name}\n"
                    f"/{token_id.replace('-', '_')}\n"
                )
            pre_result = ("\n".join(coins_list))
        elif mode == 2: # short
            for coin in response_data["coins"][:5]:
                token_id = coin["id"]
                token_name = coin["name"]
                token_symbol = coin["symbol"]
                token_rank = coin["market_cap_rank"]
                coins_list.append(
                    f"{'❓' if token_rank == None else token_rank} 🏅  <b>{token_symbol.upper()}</b> - {token_name}\n"
                    f"/{token_id.replace('-', '_')}\n"
                )
            pre_result = ("\n".join(coins_list))
        
        if not coins_list:
            result = (
                f"По запросу <b>{query}</b> ничего не найдено!"
            )
        else:
            result = (
                f"По запросу <b>{query}</b> найдено {len(coins_list)} монет:\n\n"
                f"{pre_result}"
            )
    return result


async def get_categories_list() -> str:
    """
    List all categories
    """
    async with aiohttp.ClientSession() as session:
        url = "https://api.coingecko.com/api/v3/coins/categories/list"
        
        async with session.get(url) as response:
            categories_data = await response.json()

        categories_list = []
        for item in categories_data:
            category_id = item["category_id"]
            category_name = item["name"]
            # categories_list.append(
            #     f"<b>{category_name}</b>\n/{category_id.replace('-','_')}"
            # )
            categories_list.append(
                f"/{category_id.replace('-','_')}"
            )
        result = ("\n".join(categories_list))
        final_result = (
            f"{result}"
        )
    return final_result


async def get_categories_data(category: str) -> str:
    """
    List all categories with market data
    """
    async with aiohttp.ClientSession() as session:
        url = (
            "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&"
            "category="+str(category)+"&order=market_cap_desc&per_page=100&page=1&s"
            "parkline=false&price_change_percentage=1h%2C24h%2C7d"
        )
        
        categories_url = "https://api.coingecko.com/api/v3/coins/categories"

        async with session.get(url) as response:
            categories_data = await response.json()
            
        async with session.get(categories_url) as categories_response:
            categories_resp = await categories_response.json()

        categories_dict = dict()
        categories_list = []
        
        for unit in categories_resp:
            categories_id =  unit["id"]
            categories_name = unit["name"]
            categories_market_cap = int(unit["market_cap"])
            categories_volume = int(unit["volume_24h"])
            categories_market_cap_change_24h = unit["market_cap_change_24h"]

            categories_dict[categories_id] = [
                categories_name, categories_market_cap, 
                categories_volume, categories_market_cap_change_24h
            ]
            
        for item in categories_data[:15]:
            coin_name = item["name"]
            coin_symbol = item["symbol"]
            current_price = item["current_price"]
            high_price = "{0:,}".format(current_price).replace(",", " ")
            low_price = "{:.2f}".format(current_price)
            very_low_price = "{:.5f}".format(current_price)
            formatted_current_price = (
                very_low_price if current_price < 0.009 else (
                    low_price if len(str(current_price)) > 5 else high_price
                )
            )
            categories_list.append(
                f"/{coin_symbol} <b>{coin_name}</b> - {formatted_current_price} $"
            )
            result = ("\n".join(categories_list))

        if category in categories_dict.keys():
            category_extra_list = categories_dict[category]
            category_name = category_extra_list[0]
            category_market_cap = "{:,}".format(category_extra_list[1]).replace(",", " ")
            category_volume = "{:,}".format(category_extra_list[2]).replace(",", " ")
            category_market_cap_change = float(("{:.1f}".format(category_extra_list[3]).replace(",", " ")))
            emoji_market_cap_change_24h = ('📈' if category_market_cap_change > 0 else '📉')
            final_result = (
            f"Лучшие валюты в категории \n<b>{category_name}</b>\n/{category.replace('-', '_')}\n\n"
            f"📊 Рыночная капитализация: \n"
            f"<b>$ {category_market_cap}</b> {emoji_market_cap_change_24h} <b>{category_market_cap_change}%</b>\n"
            f"📊 Объем торгов за 24 часа: <b>\n$ {category_volume}</b>\n\n"
            f"{result}"
        )
        else: 
            final_result = (
            f"Лучшие валюты в категории {category}:\n\n{result}"
        )
    return final_result
        

async def get_categories_list_data(order) -> str:
    async with aiohttp.ClientSession() as session:
        url = "https://api.coingecko.com/api/v3/coins/categories?order="+order

        async with session.get(url) as response:
            categories_list = await response.json()

        info_list = []
        
        for item in categories_list[:10]:
            coin_id = item["id"]
            coin_name = item["name"]
            market_cap = int(item["market_cap"])
            volume_24h = int(item["volume_24h"])
            formatted_market_cap = "{:,}".format(market_cap).replace(",", " ")
            formatted_volume_24h = "{:,}".format(volume_24h).replace(",", " ")
            market_cap_change_24h = float(("{:.1f}".format(item["market_cap_change_24h"]).replace(",", " ")))
            info_list.append(
                f"<b>{coin_name}</b>\n"
                f"/{coin_id}\n"      
            )
            # [:10]
            # rr_data.append(
            #     f"<b>{coin_name}</b>\n"
            #     f"/{coin_id}\n"
            #     f"📊 <b>Капитализация:</b> "
            #     f"{'📈' if market_cap_change_24h > 0 else '📉'} {market_cap_change_24h}%\n"
            #     f"{formatted_market_cap} <b>$</b>\n"
            #     f"📊 <b>Объём за 24ч:</b> \n"
            #     f"{formatted_volume_24h} <b>$</b>"         
            # )
        
        final_page = ("\n".join(info_list))
        result = (
            f"{final_page.replace('-', '_')}"
        )
    return result


async def get_trending_coins() -> str:
    """
    Top-7 trending coins on CoinGecko as searched by users 
    in the last 24 hours (Ordered by most popular first)
    """
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.coingecko.com/api/v3/search/trending") as response:
            trend_coins = await response.json()

        trend_list = []
        
        for coins in trend_coins["coins"]:
            name = coins["item"]["name"]
            symbol = coins["item"]["symbol"]
            cap = coins["item"]["market_cap_rank"]
    
            trend_list.append(
                f"#{cap} - /{symbol.lower()} - <b>{name.upper()}</b>"
            )
    return("\n".join(trend_list))