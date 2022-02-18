import aiohttp


async def get_trending_coins():
    """
    Top-7 trending coins on CoinGecko as searched by users 
    in the last 24 hours (Ordered by most popular first)
    """
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingecko.com/api/v3/search/trending') as response:
            trend_coins = await response.json()

        trend_list = []
        
        for coins in trend_coins['coins']:
            name = coins["item"]["name"]
            symbol = coins["item"]["symbol"]
            cap = coins["item"]["market_cap_rank"]
            trend_list.append(f'#{cap}   {symbol}  -  {name} ')
        
        return('\n'.join(trend_list))