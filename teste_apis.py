import requests
import json

url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

if response.ok:
    with open("exemplo_request.json", "w") as file:
        json.dump(response.json(), file)
