import csv
import aiohttp
import asyncio
from itertools import zip_longest


def name_changer():
    with open("/Users/keyglock/Documents/python/CryptoCurrency/CoinGecko Token API List - CoinGecko Token API List.csv", mode="r") as csv_data:
        reader = csv.reader(csv_data)    
        token_id_list = [rows[0] for rows in reader]
        # token_symbol_list = [rows[1] for rows in reader] # TODO
        # token_name_list = [rows[2] for rows in reader]
    new_token_list = [word.replace("-", "_") for word in token_id_list]
    # print("[*] Tokens names with signs '-' changed to '_' successfully!")

    data = [token_id_list, new_token_list]
    export_data = zip_longest(*data, fillvalue = '')
    with open('CG_token_list.csv', 'w', encoding="ISO-8859-1", newline='') as file:
        write = csv.writer(file)
        write.writerow(("Id", "Extra"))
        write.writerows(export_data)
    result = "[*] The original and additional names are written to a new CSV file!"
    return result


async def categories_list_changer():
    """
    List all categories and save to CSV with extra named categories
    """
    async with aiohttp.ClientSession() as session:
        url = "https://api.coingecko.com/api/v3/coins/categories/list"
        
        async with session.get(url) as response:
            categories_data = await response.json()
        
        categories_id = []
        categories_name = []
        
        for item in categories_data:
            category_id = item["category_id"]
            category_name = item["name"]
            categories_id.append(category_id)
            categories_name.append(category_name)

        extra_categories_id = [word.replace("-", "_") for word in categories_id]

        data = [categories_id, extra_categories_id, categories_name]
        export_data = zip_longest(*data, fillvalue = '')

        with open('CG_categories_list.csv', 'w', encoding="ISO-8859-1", newline='') as file:
            write = csv.writer(file)
            write.writerow(("ID", "Extra", "Name"))
            write.writerows(export_data)
        result = "[*] The original and additional names are written to a new CSV file!"
    return result


if __name__ == '__main__':
    # name_changer()
    asyncio.run(categories_list_changer())