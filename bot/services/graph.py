import aiohttp
import asyncio
import datetime
# pip pandas pyplot
import pandas as pd
import matplotlib.pyplot as plt


async def get_graph_data(token: str, days: int):
    """
    Get historical market data include price, market cap, and 24h volume
    """
    async with aiohttp.ClientSession() as session:
        url = f"https://api.coingecko.com/api/v3/coins/"+token+"/market_chart?vs_currency=usd&days="+str(days)
        today = datetime.datetime.today()

        async with session.get(url) as response:
            graph_data = await response.json()

            time_list = []
            price_list = []
            token_price = graph_data["prices"]

            for i in token_price:
                price_list.append(i[1])

            for x in range(0, int(days)+1):
                time_list.append((today - datetime.timedelta(days = x)).strftime('%Y-%m-%d'))

            time_list = time_list[::-1]

            df = pd.DataFrame({"Date": time_list})
            df["Price"]=pd.DataFrame({'Price': price_list})

            print(df)

            # img = mpimg.imread("test1.jpeg") # TODO
            df.plot(x='Date',y='Price', figsize=(5,2))
            plt.axis('off')
            plt.savefig(f"{token}_{days}d.png")
            # plt.show()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_graph_data("bitcoin", 365))