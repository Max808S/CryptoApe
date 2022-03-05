import csv

# with open("CoinGecko Token API List - CoinGecko Token API List.csv", newline="") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['Id'], row['Symbol'], row['Name'])

# print(row)


with open('CoinGecko Token API List - CoinGecko Token API List.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)