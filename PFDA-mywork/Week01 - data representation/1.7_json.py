# https://api.coindesk.com/v1/bpi/currentprice.json
# Write a program that will print this JSON to the console
# Author: Irene Kilgannon

import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url)
data = response.json()
print(data)

# Modify the program to only output the current price of euro

print(data['bpi']['EUR']['rate_float'])