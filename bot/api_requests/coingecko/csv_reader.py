from csv import reader
import csv


with open('/Users/keyglock/Documents/python/CryptoCurrency/CG_categories_list.csv', mode='r') as cg_categories_csv_data:
# with open('/root/TgBot/CryptoCurrency/CG_categories_list.csv', mode='r') as cg_categories_csv_data:
    reader = csv.reader(cg_categories_csv_data)
    dict_from_cg_categories_csv = {rows[0]:rows[1] for rows in reader}

cg_categories_keys = dict_from_cg_categories_csv.keys()
cg_categories_values = list(dict_from_cg_categories_csv.values())


# EXAMPLE: tron-eth - tron_eth
with open("/Users/keyglock/Documents/python/CryptoCurrency/CG_token_list.csv", mode="r") as csv_data:
# with open("/root/TgBot/CryptoCurrency/CG_token_list.csv", mode="r") as csv_data:
    reader = csv.reader(csv_data)
    dict_with_token_ids = {rows[0]:rows[1] for rows in reader}

# ID: tron-tron
cg_token_name = list(dict_with_token_ids.keys()) 
# EXTRA: tron_tron
cg_token_extra_name = list(dict_with_token_ids.values())


# EXAMPLE: bitcoin - btc
with open("/Users/keyglock/Documents/python/CryptoCurrency/CoinGecko_Token_API_List_-_CoinGecko_Token_API_List.csv", mode="r") as csv_data:
# with open("/root/TgBot/CryptoCurrency/CoinGecko_Token_API_List_-_CoinGecko_Token_API_List.csv", mode="r") as csv_data:
    reader = csv.reader(csv_data)
    dict_from_tokens_csv = {rows[0]:rows[1] for rows in reader}

# ID: bitcoin
cg_tokens_keys = list(dict_from_tokens_csv.keys())
# SYMBOL: btc
cg_tokens_values = list(dict_from_tokens_csv.values())


# EXAMPLE: bitcoin - Bitcoin (name)
with open('/Users/keyglock/Documents/python/CryptoCurrency/CoinGecko_Token_API_List_-_CoinGecko_Token_API_List.csv', mode='r') as extra_csv_data:
# with open('/root/TgBot/CryptoCurrency/CoinGecko_Token_API_List_-_CoinGecko_Token_API_List.csv', mode='r') as extra_csv_data:
    extra_reader = csv.reader(extra_csv_data)
    extra_dict_from_tokens_csv = {column[0]:column[2] for column in extra_reader}

# ID: bitcoin
extra_cg_token_keys = list(extra_dict_from_tokens_csv.keys())
# NAME: Bitcoin 
extra_cg_token_values = list(extra_dict_from_tokens_csv.values())


# if __name__ == '__main__':
    # print(cg_tokens_keys) # bitcoin (ID)
    # print(cg_tokens_values) # btc (symb)
    # print(extra_dict_from_tokens_csv.items())
    # print(extra_cg_token_keys) # bitcoin (ID)
    # print(extra_cg_token_values) # Bitcoin (name)