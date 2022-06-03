import aiohttp


async def get_tokens_stat(sort: str, res: str, page: int) -> str:
    """
    Getting tokens stat view
    /api/v3/coins/markets
    """
    async with aiohttp.ClientSession() as session: 
        # url = (
        #     f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&"
        #     f"order=+{sort}+&per_page=100&page=1&sparkline=false&"
        #     f"price_change_percentage=1h%2C24h%2C7d"
        # )

        if sort == "market_cap_desc":
            url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d"
        elif sort == "volume_desc":
            url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=volume_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d"

        tokens_price_list = []
        tokens_rank_list = []
        tokens_name_list = []
        tokens_symbol_list = []
        token_1h_list = []
        token_24h_list = []
        token_7d_list = []
        market_cap_list = []
        total_volume_list = []
        emoji_1h_list = []
        emoji_24h_list = []
        emoji_7d_list = []

        async with session.get(url) as response:
            tokens_data = await response.json()

            if page == 1:
                coin_data = tokens_data[:10]
                page_info = "[1 - 10]"
            elif page == 2:
                coin_data = tokens_data[10:20]
                page_info = "[11 - 20]"
            elif page == 3:
                coin_data = tokens_data[20:30]
                page_info = "[21 - 30]"
            elif page == 4:
                coin_data = tokens_data[30:40]
                page_info = "[31 - 40]"
            elif page == 5:
                coin_data = tokens_data[40:50]
                page_info = "[41 - 50]"
            elif page == 6:
                coin_data = tokens_data[50:60]
                page_info = "[51 - 60]"
            elif page == 7:
                coin_data = tokens_data[60:70]
                page_info = "[61 - 70]"
            elif page == 8:
                coin_data = tokens_data[70:80]
                page_info = "[71 - 80]"
            elif page == 9:
                coin_data = tokens_data[80:90]
                page_info = "[81 - 90]"
            elif page == 10:
                coin_data = tokens_data[90:100]
                page_info = "[91 - 100]"
           
            for token in coin_data: 
                token_name = token["name"]
                token_symbol = token["symbol"]
                token_price = token["current_price"]
                coin_cap_rank = token["market_cap_rank"]
                market_cap = token["market_cap"]
                total_volume = token["total_volume"]
                percent_change_1h = token["price_change_percentage_1h_in_currency"]
                percent_change_24h = token["price_change_percentage_24h_in_currency"]
                percent_change_7d = token["price_change_percentage_7d_in_currency"]
                
                # current price
                formatted_token_price = "❓" if token_price == None else (
                    ("{:.2f}".format(token_price)) if len(str(token_price)) > 5 else (
                        "{0:,}".format(token_price).replace(",", " ")
                    )
                )

                # token stats
                formatted_market_cap = "❓" if market_cap == None else (
                    "❓" if market_cap == 0 else ("{0:,}".format(market_cap).replace(",", " "))
                )

                formatted_volume = "❓" if total_volume == None else (
                    "❓" if total_volume == 0 else ("{0:,}".format(total_volume).replace(",", " "))
                )

                formatted_coin_rank = "❓" if coin_cap_rank == None else coin_cap_rank

                h1_emoji = "⚠️" if percent_change_1h == None else ("📈" if percent_change_1h > 0 else "📉")
                h24_emoji = "⚠️" if percent_change_24h == None else ("📈" if percent_change_24h > 0 else "📉")
                d7_emoji = "⚠️" if percent_change_7d == None else ("📈" if percent_change_7d > 0 else "📉")

                tokens_name_list.append(token_name)
                tokens_symbol_list.append(token_symbol)
                tokens_price_list.append(formatted_token_price)
                tokens_rank_list.append(formatted_coin_rank)
                market_cap_list.append(formatted_market_cap)
                total_volume_list.append(formatted_volume)
                emoji_1h_list.append(h1_emoji)
                emoji_24h_list.append(h24_emoji)
                emoji_7d_list.append(d7_emoji)
                token_1h_list.append("❓" if percent_change_24h == None else float("{:.1f}".format(percent_change_1h)))
                token_24h_list.append("❓" if percent_change_24h == None else float("{:.1f}".format(percent_change_24h)))
                token_7d_list.append("❓" if percent_change_7d == None else float("{:.1f}".format(percent_change_7d)))

            market_cap_result = (
                f"Криптовалюты сортированы по <b>рыночной капитализации</b>:\n"
                f"\n#{tokens_rank_list[0]} <b>{tokens_name_list[0]}</b> - /{tokens_symbol_list[0]} - {tokens_price_list[0]} <b>$</b>\n"
                f"📊 {market_cap_list[0]} <b>$</b>\n"
                f"\n#{tokens_rank_list[1]} <b>{tokens_name_list[1]}</b> - /{tokens_symbol_list[1]} - {tokens_price_list[1]} <b>$</b>\n"
                f"📊 {market_cap_list[1]} <b>$</b>\n"
                f"\n#{tokens_rank_list[2]} <b>{tokens_name_list[2]}</b> - /{tokens_symbol_list[2]} - {tokens_price_list[2]} <b>$</b>\n"
                f"📊 {market_cap_list[2]} <b>$</b>\n"
                f"\n#{tokens_rank_list[3]} <b>{tokens_name_list[3]}</b> - /{tokens_symbol_list[3]} - {tokens_price_list[3]} <b>$</b>\n"
                f"📊 {market_cap_list[3]} <b>$</b>\n"
                f"\n#{tokens_rank_list[4]} <b>{tokens_name_list[4]}</b> - /{tokens_symbol_list[4]} - {tokens_price_list[4]} <b>$</b>\n"
                f"📊 {market_cap_list[4]} <b>$</b>\n"
                f"\n#{tokens_rank_list[5]} <b>{tokens_name_list[5]}</b> - /{tokens_symbol_list[5]} - {tokens_price_list[0]} <b>$</b>\n"
                f"📊 {market_cap_list[5]} <b>$</b>\n"
                f"\n#{tokens_rank_list[6]} <b>{tokens_name_list[6]}</b> - /{tokens_symbol_list[6]} - {tokens_price_list[1]} <b>$</b>\n"
                f"📊 {market_cap_list[6]} <b>$</b>\n"
                f"\n#{tokens_rank_list[7]} <b>{tokens_name_list[7]}</b> - /{tokens_symbol_list[7]} - {tokens_price_list[2]} <b>$</b>\n"
                f"📊 {market_cap_list[7]} <b>$</b>\n"
                f"\n#{tokens_rank_list[8]} <b>{tokens_name_list[8]}</b> - /{tokens_symbol_list[8]} - {tokens_price_list[3]} <b>$</b>\n"
                f"📊 {market_cap_list[8]} <b>$</b>\n"
                f"\n#{tokens_rank_list[9]} <b>{tokens_name_list[9]}</b> - /{tokens_symbol_list[9]} - {tokens_price_list[4]} <b>$</b>\n"
                f"📊 {market_cap_list[9]} <b>$</b>\n"
                f"\nСтраница: <b>{page}</b> {page_info}"
            )

            total_volume_result = (
                f"Криптовалюты сортированы по <b>объему торгов за 24ч</b>:\n"
                f"\n#{tokens_rank_list[0]} <b>{tokens_name_list[0]}</b> - /{tokens_symbol_list[0]} - {tokens_price_list[0]} <b>$</b>\n"
                f"📊 {total_volume_list[0]} <b>$</b>\n"
                f"\n#{tokens_rank_list[1]} <b>{tokens_name_list[1]}</b> - /{tokens_symbol_list[1]} - {tokens_price_list[1]} <b>$</b>\n"
                f"📊 {total_volume_list[1]} <b>$</b>\n"
                f"\n#{tokens_rank_list[2]} <b>{tokens_name_list[2]}</b> - /{tokens_symbol_list[2]} - {tokens_price_list[2]} <b>$</b>\n"
                f"📊 {total_volume_list[2]} <b>$</b>\n"
                f"\n#{tokens_rank_list[3]} <b>{tokens_name_list[3]}</b> - /{tokens_symbol_list[3]} - {tokens_price_list[3]} <b>$</b>\n"
                f"📊 {total_volume_list[3]} <b>$</b>\n"
                f"\n#{tokens_rank_list[4]} <b>{tokens_name_list[4]}</b> - /{tokens_symbol_list[4]} - {tokens_price_list[4]} <b>$</b>\n"
                f"📊 {total_volume_list[4]} <b>$</b>\n"
                f"\n#{tokens_rank_list[5]} <b>{tokens_name_list[5]}</b> - /{tokens_symbol_list[5]} - {tokens_price_list[0]} <b>$</b>\n"
                f"📊 {total_volume_list[5]} <b>$</b>\n"
                f"\n#{tokens_rank_list[6]} <b>{tokens_name_list[6]}</b> - /{tokens_symbol_list[6]} - {tokens_price_list[1]} <b>$</b>\n"
                f"📊 {total_volume_list[6]} <b>$</b>\n"
                f"\n#{tokens_rank_list[7]} <b>{tokens_name_list[7]}</b> - /{tokens_symbol_list[7]} - {tokens_price_list[2]} <b>$</b>\n"
                f"📊 {total_volume_list[7]} <b>$</b>\n"
                f"\n#{tokens_rank_list[8]} <b>{tokens_name_list[8]}</b> - /{tokens_symbol_list[8]} - {tokens_price_list[3]} <b>$</b>\n"
                f"📊 {total_volume_list[8]} <b>$</b>\n"
                f"\n#{tokens_rank_list[9]} <b>{tokens_name_list[9]}</b> - /{tokens_symbol_list[9]} - {tokens_price_list[4]} <b>$</b>\n"
                f"📊 {total_volume_list[9]} <b>$</b>\n"
                f"\nСтраница: <b>{page}</b> {page_info}"
            )

            h1_result = (
                f"Криптовалюты сортированы по <b>рыночной капитализации</b>:"
                f"\n\n<b>{tokens_name_list[0]}</b>  /{tokens_symbol_list[0]} - {tokens_price_list[0]} <b>$</b> {emoji_1h_list[0]} {token_1h_list[0]}%"
                f"\n\n<b>{tokens_name_list[1]}</b>  /{tokens_symbol_list[1]} - {tokens_price_list[1]} <b>$</b> {emoji_1h_list[1]} {token_1h_list[1]}%"
                f"\n\n<b>{tokens_name_list[2]}</b>  /{tokens_symbol_list[2]} - {tokens_price_list[2]} <b>$</b> {emoji_1h_list[2]} {token_1h_list[2]}%"
                f"\n\n<b>{tokens_name_list[3]}</b>  /{tokens_symbol_list[3]} - {tokens_price_list[3]} <b>$</b> {emoji_1h_list[3]} {token_1h_list[3]}%"
                f"\n\n<b>{tokens_name_list[4]}</b>  /{tokens_symbol_list[4]} - {tokens_price_list[4]} <b>$</b> {emoji_1h_list[4]} {token_1h_list[4]}%"
                f"\n\n<b>{tokens_name_list[5]}</b>  /{tokens_symbol_list[5]} - {tokens_price_list[5]} <b>$</b> {emoji_1h_list[5]} {token_1h_list[5]}%"
                f"\n\n<b>{tokens_name_list[6]}</b>  /{tokens_symbol_list[6]} - {tokens_price_list[6]} <b>$</b> {emoji_1h_list[6]} {token_1h_list[6]}%"
                f"\n\n<b>{tokens_name_list[7]}</b>  /{tokens_symbol_list[7]} - {tokens_price_list[7]} <b>$</b> {emoji_1h_list[7]} {token_1h_list[7]}%"
                f"\n\n<b>{tokens_name_list[8]}</b>  /{tokens_symbol_list[8]} - {tokens_price_list[8]} <b>$</b> {emoji_1h_list[8]} {token_1h_list[8]}%" 
                f"\n\n<b>{tokens_name_list[9]}</b>  /{tokens_symbol_list[9]} - {tokens_price_list[9]} <b>$</b> {emoji_1h_list[9]} {token_1h_list[9]}%"
                f"\n\nСтраница: <b>{page}</b> {page_info}    🕑 <b>1ч</b>"
            )

            h24_result = (
                f"Криптовалюты сортированы по <b>рыночной капитализации</b>:"
                f"\n\n<b>{tokens_name_list[0]}</b>  /{tokens_symbol_list[0]} - {tokens_price_list[0]} <b>$</b> {emoji_24h_list[0]} {token_24h_list[0]}%"
                f"\n\n<b>{tokens_name_list[1]}</b>  /{tokens_symbol_list[1]} - {tokens_price_list[1]} <b>$</b> {emoji_24h_list[1]} {token_24h_list[1]}%"
                f"\n\n<b>{tokens_name_list[2]}</b>  /{tokens_symbol_list[2]} - {tokens_price_list[2]} <b>$</b> {emoji_24h_list[2]} {token_24h_list[2]}%"
                f"\n\n<b>{tokens_name_list[3]}</b>  /{tokens_symbol_list[3]} - {tokens_price_list[3]} <b>$</b> {emoji_24h_list[3]} {token_24h_list[3]}%"
                f"\n\n<b>{tokens_name_list[4]}</b>  /{tokens_symbol_list[4]} - {tokens_price_list[4]} <b>$</b> {emoji_24h_list[4]} {token_24h_list[4]}%"
                f"\n\n<b>{tokens_name_list[5]}</b>  /{tokens_symbol_list[5]} - {tokens_price_list[5]} <b>$</b> {emoji_24h_list[5]} {token_24h_list[5]}%"
                f"\n\n<b>{tokens_name_list[6]}</b>  /{tokens_symbol_list[6]} - {tokens_price_list[6]} <b>$</b> {emoji_24h_list[6]} {token_24h_list[6]}%"
                f"\n\n<b>{tokens_name_list[7]}</b>  /{tokens_symbol_list[7]} - {tokens_price_list[7]} <b>$</b> {emoji_24h_list[7]} {token_24h_list[7]}%"
                f"\n\n<b>{tokens_name_list[8]}</b>  /{tokens_symbol_list[8]} - {tokens_price_list[8]} <b>$</b> {emoji_24h_list[8]} {token_24h_list[8]}%" 
                f"\n\n<b>{tokens_name_list[9]}</b>  /{tokens_symbol_list[9]} - {tokens_price_list[9]} <b>$</b> {emoji_24h_list[9]} {token_24h_list[9]}%"
                f"\n\nСтраница: <b>{page}</b> {page_info}    🕑 <b>24ч</b>"
            )

            d7_result = (
                f"Криптовалюты сортированы по <b>рыночной капитализации</b>:"
                f"\n\n<b>{tokens_name_list[0]}</b>  /{tokens_symbol_list[0]} - {tokens_price_list[0]} <b>$</b> {emoji_7d_list[0]} {token_7d_list[0]}%"
                f"\n\n<b>{tokens_name_list[1]}</b>  /{tokens_symbol_list[1]} - {tokens_price_list[1]} <b>$</b> {emoji_7d_list[1]} {token_7d_list[1]}%"
                f"\n\n<b>{tokens_name_list[2]}</b>  /{tokens_symbol_list[2]} - {tokens_price_list[2]} <b>$</b> {emoji_7d_list[2]} {token_7d_list[2]}%"
                f"\n\n<b>{tokens_name_list[3]}</b>  /{tokens_symbol_list[3]} - {tokens_price_list[3]} <b>$</b> {emoji_7d_list[3]} {token_7d_list[3]}%"
                f"\n\n<b>{tokens_name_list[4]}</b>  /{tokens_symbol_list[4]} - {tokens_price_list[4]} <b>$</b> {emoji_7d_list[4]} {token_7d_list[4]}%"
                f"\n\n<b>{tokens_name_list[5]}</b>  /{tokens_symbol_list[5]} - {tokens_price_list[5]} <b>$</b> {emoji_7d_list[5]} {token_7d_list[5]}%"
                f"\n\n<b>{tokens_name_list[6]}</b>  /{tokens_symbol_list[6]} - {tokens_price_list[6]} <b>$</b> {emoji_7d_list[6]} {token_7d_list[6]}%"
                f"\n\n<b>{tokens_name_list[7]}</b>  /{tokens_symbol_list[7]} - {tokens_price_list[7]} <b>$</b> {emoji_7d_list[7]} {token_7d_list[7]}%"
                f"\n\n<b>{tokens_name_list[8]}</b>  /{tokens_symbol_list[8]} - {tokens_price_list[8]} <b>$</b> {emoji_7d_list[8]} {token_7d_list[8]}%" 
                f"\n\n<b>{tokens_name_list[9]}</b>  /{tokens_symbol_list[9]} - {tokens_price_list[9]} <b>$</b> {emoji_7d_list[9]} {token_7d_list[9]}%"
                f"\n\nСтраница: <b>{page}</b> {page_info}    🕑 <b>7д</b>"
            )

            percentage_result = (
                f"<b>{tokens_name_list[0]}</b> - /{tokens_symbol_list[0]} - {tokens_price_list[0]} <b>$</b>\n"
                f"{emoji_1h_list[0]} <b>24 ч:</b>  {token_1h_list[0]}%\n"
                f"{emoji_24h_list[5]} <b>7 дней:</b> {token_24h_list[0]}%\n"
                f"{d7_emoji} <b>30 дней:</b> {token_7d_list[0]}%\n"
                f"\n<b>{tokens_name_list[1]}</b> - /{tokens_symbol_list[1]} - {tokens_price_list[1]} <b>$</b>\n"
                f"{emoji_1h_list[0]} <b>24 ч:</b>  {token_1h_list[1]}%\n"
                f"{emoji_24h_list[5]} <b>7 дней:</b> {token_24h_list[1]}%\n"
                f"{d7_emoji} <b>30 дней:</b> {token_7d_list[1]}%\n"
                f"\n<b>{tokens_name_list[2]}</b> - /{tokens_symbol_list[2]} - {tokens_price_list[2]} <b>$</b>\n"
                f"{emoji_1h_list[0]} <b>24 ч:</b>  {token_1h_list[2]}%\n"
                f"{emoji_24h_list[5]} <b>7 дней:</b> {token_24h_list[2]}%\n"
                f"{d7_emoji} <b>30 дней:</b> {token_7d_list[2]}%\n"
                f"\n<b>{tokens_name_list[3]}</b> - /{tokens_symbol_list[3]} - {tokens_price_list[3]} <b>$</b>\n"
                f"{emoji_1h_list[0]} <b>24 ч:</b>  {token_1h_list[3]}%\n"
                f"{emoji_24h_list[5]} <b>7 дней:</b> {token_24h_list[3]}%\n"
                f"{d7_emoji} <b>30 дней:</b> {token_7d_list[3]}%\n"
                f"\n<b>{tokens_name_list[4]}</b> - /{tokens_symbol_list[4]} - {tokens_price_list[4]} <b>$</b>\n"
                f"{emoji_1h_list[0]} <b>24 ч:</b>  {token_1h_list[4]}%\n"
                f"{emoji_24h_list[5]} <b>7 дней:</b> {token_24h_list[4]}%\n"
                f"{emoji_24h_list[5]} <b>30 дней:</b> {token_7d_list[4]}%\n"
            )

            # mc_volume = (
            #     f"<b>{tokens_name_list[0]}</b> - /{tokens_symbol_list[0]} - {tokens_price_list[0]} <b>$</b>\n"
            #     f"📊 <b>Капитализация:</b> \n{market_cap_list[0]} <b>$</b>\n"
            #     f"📊 <b>Объём за 24ч:</b> \n{total_volume_list[0]} <b>$</b>\n"
            #     f"\n<b>{tokens_name_list[1]}</b> - /{tokens_symbol_list[1]} - {tokens_price_list[1]} <b>$</b>\n"
            #     f"📊 <b>Капитализация:</b> \n{market_cap_list[1]} <b>$</b>\n"
            #     f"📊 <b>Объём за 24ч:</b> \n{total_volume_list[1]} <b>$</b>\n"
            #     f"\n<b>{tokens_name_list[2]}</b> - /{tokens_symbol_list[2]} - {tokens_price_list[2]} <b>$</b>\n"
            #     f"📊 <b>Капитализация:</b> \n{market_cap_list[2]} <b>$</b>\n"
            #     f"📊 <b>Объём за 24ч:</b> \n{total_volume_list[2]} <b>$</b>\n"
            #     f"\n<b>{tokens_name_list[3]}</b> - /{tokens_symbol_list[3]} - {tokens_price_list[3]} <b>$</b>\n"
            #     f"📊 <b>Капитализация:</b> \n{market_cap_list[3]} <b>$</b>\n"
            #     f"📊 <b>Объём за 24ч:</b> \n{total_volume_list[3]} <b>$</b>\n"
            #     f"\n<b>{tokens_name_list[4]}</b> - /{tokens_symbol_list[4]} - {tokens_price_list[4]} <b>$</b>\n"
            #     f"📊 <b>Капитализация:</b> \n{market_cap_list[4]} <b>$</b>\n"
            #     f"📊 <b>Объём за 24ч:</b> \n{total_volume_list[4]} <b>$</b>\n"
            #     # f"Page: {page}"
            # )

    if res == "percentage": 
        return percentage_result
    elif res == "market_cap":
        return market_cap_result
    elif res == "total_volume":
        return total_volume_result
    elif res == "h1_result":
        return h1_result
    elif res == "h24_result":
        return h24_result
    elif res == "d7_result":
        return d7_result
    else: return "404 :)" # TODO


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