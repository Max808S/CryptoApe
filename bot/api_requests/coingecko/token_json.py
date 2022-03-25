import csv


with open('CoinGecko_Token_API_List_-_CoinGecko_Token_API_List.csv', mode='r') as csv_data:
    reader = csv.reader(csv_data)
    dict_from_tokens_csv = {rows[0]:rows[1] for rows in reader}
    
cg_tokens_keys = list(dict_from_tokens_csv.keys())
cg_tokens_values = list(dict_from_tokens_csv.values())


with open('CG_Categories.csv', mode='r') as cg_categories_csv_data:
    reader = csv.reader(cg_categories_csv_data)
    dict_from_cg_categories_csv = {rows[0]:rows[1] for rows in reader}

cg_categories_keys = list(dict_from_cg_categories_csv.keys())
cg_categories_values = list(dict_from_cg_categories_csv.values())