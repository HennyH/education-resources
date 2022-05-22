#!/usr/bin/env python3
import cgi
import datetime
import cgitb
import json
from urllib.request import Request, urlopen

cgitb.enable()

crypto_name = "monero"
crypto_name_abbrev = "XMR"
req = Request(url=f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=aud")
req.add_header("Accept", "application/json")

with urlopen(req) as response:
    json_response = response.read().decode("utf-8")
    price = json.loads(json_response)

print("Content-Type: text/html")
print()
print(f"<h1>{crypto_name_abbrev} ${price[crypto_name]['aud']} AUD</h1")
