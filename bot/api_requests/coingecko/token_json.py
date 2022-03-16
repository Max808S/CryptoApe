import csv


with open('CoinGecko Token API List - CoinGecko Token API List.csv', mode='r') as csv_data:
    reader = csv.reader(csv_data)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}
    
csv_keys = list(dict_from_csv.keys())
csv_values = list(dict_from_csv.values())


with open('CG Categories.csv', mode='r') as cg_categories_csv_data:
    reader = csv.reader(cg_categories_csv_data)
    dict_from_cg_categories_csv = {rows[0]:rows[1] for rows in reader}

cg_categories_keys = list(dict_from_cg_categories_csv.keys())
cg_categories_values = list(dict_from_cg_categories_csv.values())