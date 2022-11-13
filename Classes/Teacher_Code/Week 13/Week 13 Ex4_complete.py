# Use the CoinDesk API to get live Bitcoin price
# Locate the price information inside the JSON
# https://api.coindesk.com/v1/bpi/currentprice/USD.json

import requests
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")

if response:
    data = json.loads(response.text)
    print(json.dumps(data, indent = 4))
    price = data["bpi"]["USD"]["rate_float"]
    print("Live Bitcoin price:", price)
    
else:
    print("Could not connect successfully.")