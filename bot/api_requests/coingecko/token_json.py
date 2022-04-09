import csv
import aiohttp

from csv import reader
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


async def categories_list_changer() -> str:
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


# with open('/Users/keyglock/Documents/python/CryptoCurrency/CG_categories_list.csv', mode='r') as cg_categories_csv_data:
with open('/root/TgBot/CryptoCurrency/CG_categories_list.csv', mode='r') as cg_categories_csv_data:
    reader = csv.reader(cg_categories_csv_data)
    dict_from_cg_categories_csv = {rows[0]:rows[1] for rows in reader}

cg_categories_keys = dict_from_cg_categories_csv.keys()
cg_categories_values = list(dict_from_cg_categories_csv.values())


# EXAMPLE: tron-eth - tron_eth
# with open("/Users/keyglock/Documents/python/CryptoCurrency/CG_token_list.csv", mode="r") as csv_data:
with open("/root/TgBot/CryptoCurrency/CG_token_list.csv", mode="r") as csv_data:
    reader = csv.reader(csv_data)
    dict_with_token_ids = {rows[0]:rows[1] for rows in reader}

# ID: tron-tron
cg_token_name = list(dict_with_token_ids.keys()) 
# EXTRA: tron_tron
cg_token_extra_name = list(dict_with_token_ids.values())


# EXAMPLE: bitcoin - btc
# with open("/Users/keyglock/Documents/python/CryptoCurrency/CoinGecko_Token_API_List_-_CoinGecko_Token_API_List.csv", mode="r") as csv_data:
with open("/root/TgBot/CryptoCurrency/CoinGecko_Token_API_List_-_CoinGecko_Token_API_List.csv", mode="r") as csv_data:
    reader = csv.reader(csv_data)
    dict_from_tokens_csv = {rows[0]:rows[1] for rows in reader}

# ID: bitcoin
cg_tokens_keys = list(dict_from_tokens_csv.keys())
# SYMBOL: btc
cg_tokens_values = list(dict_from_tokens_csv.values())


# EXAMPLE: bitcoin - Bitcoin (name)
# with open('/Users/keyglock/Documents/python/CryptoCurrency/CoinGecko_Token_API_List_-_CoinGecko_Token_API_List.csv', mode='r') as extra_csv_data:
with open('/root/TgBot/CryptoCurrency/CoinGecko_Token_API_List_-_CoinGecko_Token_API_List.csv', mode='r') as extra_csv_data:
    extra_reader = csv.reader(extra_csv_data)
    extra_dict_from_tokens_csv = {column[0]:column[2] for column in extra_reader}

# ID: bitcoin
extra_cg_token_keys = list(extra_dict_from_tokens_csv.keys())
# NAME: Bitcoin 
extra_cg_token_values = list(extra_dict_from_tokens_csv.values())


# if __name__ == '__main__':
    # name_changer()
    # print(cg_tokens_keys) # bitcoin (ID)
    # print(cg_tokens_values) # btc (symb)
    # print(extra_dict_from_tokens_csv.items())
    # print(extra_cg_token_keys) # bitcoin (ID)
    # print(extra_cg_token_values) # Bitcoin (name)