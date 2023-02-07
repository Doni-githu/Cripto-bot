# import json
# import requests
#
# url = "https://coinranking1.p.rapidapi.com/coins"
#
# querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl", "timePeriod": "24h", "tiers[0]": "1", "orderBy": "marketCap",
#                "orderDirection": "desc", "limit": "50", "offset": "0"}
#
# headers = {
#     "X-RapidAPI-Key": "309762a3f1mshb8816378be4c2bcp1e702fjsn568bcbe3baf1",
#     "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
# }
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# x = json.loads(response.text)
# data = x['data']
# coins = data['coins']
# name2 = ""
# for i in range(len(coins)):
#     name2 += f"{coins[i]['symbol']} - {coins[i]['name']}\n"
# print(name2)
