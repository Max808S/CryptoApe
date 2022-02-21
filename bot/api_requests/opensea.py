# import logging
# import requests

#  TODO

# def CollectionStat(slug=str, username=str, user_id=int):
#     try:
#         url = 'https://api.opensea.io/api/v1/collection/'+slug+'/stats'
#         headers = {"Accept": "application/json"}
#         response = requests.request("GET", url, headers=headers)
#         data = response.json()
#         # one day (1)
#         one_day_volume = data["stats"]["one_day_volume"]
#         one_day_change = data["stats"]["one_day_change"]
#         one_day_sales = data["stats"]["one_day_sales"]
#         one_day_average_price = data["stats"]["one_day_average_price"]
#         # seven days (7)
#         seven_day_volume = data["stats"]["seven_day_volume"]
#         seven_day_change = data["stats"]["seven_day_change"]
#         seven_day_sales = data["stats"]["seven_day_sales"]
#         seven_day_average_price = data["stats"]["seven_day_average_price"]
#         # thirty days (14)
#         thirty_day_volume = data["stats"]["thirty_day_volume"]
#         thirty_day_change = data["stats"]["thirty_day_change"]
#         thirty_day_sales = data["stats"]["thirty_day_sales"]
#         thirty_day_average_price = data["stats"]["thirty_day_average_price"]   
#         # total
#         total_volume = data["stats"]["total_volume"]
#         total_sales = data["stats"]["total_sales"]
#         total_supply = data["stats"]["total_supply"]
#         num_owners = data["stats"]["num_owners"]
#         # average_price = data["stats"]["average_price"]
#         market_cap = data["stats"]["market_cap"]
#         floor_price = data["stats"]["floor_price"]
        
#         result = f'Коллекция: {slug}' \
#                     f'\nМинимальная цена: {floor_price} eth.' \
#                     f'\nВладельцев NFT: {num_owners}' \
#                     f'\nКоличество NFT: {int(total_supply)}' \
#                     f'\n' \
#                     f'\nВсего продаж: {int(total_sales)}' \
#                     f'\nОбъем продаж: {float("{:.2f}".format(total_volume))} eth.' \
#                     f'\nКапитализация: {float("{:.2f}".format(market_cap))} eth.' \
#                     f'\n' \
#                     f'\nПродано сегодня: {int(one_day_sales)} nfts.' \
#                     f'\nОбъем за один день: {float("{:.2f}".format(one_day_volume))} eth.' \
#                     f'\nСегодняшние изменения: {float("{:.2f}".format(one_day_change))}%' \
#                     f'\nСредняя цена сегодня: {float("{:.2f}".format(one_day_average_price))} eth.' \
#                     f'\n' \
#                     f'\nПродано за 7 дней: {int(seven_day_sales)} nfts.' \
#                     f'\nОбъем за 7 дней: {float("{:.2f}".format(seven_day_volume))} eth.' \
#                     f'\nИзменения за 7 дней: {float("{:.2f}".format(seven_day_change))}%' \
#                     f'\nСредняя цена за 7 дней: {float("{:.2f}".format(seven_day_average_price))} eth.' \
#                     f'\n' \
#                     f'\nПродано за 14 дней: {int(thirty_day_sales)} nfts.' \
#                     f'\nОбъем за 14 дней: {float("{:.2f}".format(thirty_day_volume))} eth.' \
#                     f'\nИзменения за 14 дней: {float("{:.2f}".format(thirty_day_change))}%' \
#                     f'\nСредняя цена за 14 дней: {float("{:.2f}".format(thirty_day_average_price))} eth.'
#         logging.info(f'User {username} ID: {user_id} checked NFT collection {slug}')
#         # print(result)
#         return result
#     except Exception as ex:
#         logging.info(f'{ex} \nWARNING! User: {username} ID: {user_id} has not received data!')


# # if __name__ == '__main__':
# #     CollectionStat('cool-cats-nft', 'Maxim', 123)