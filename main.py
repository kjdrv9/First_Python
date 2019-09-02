import os
import sys
import urllib.request
import json

url = "https://blockchain.info/ticker"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if (rescode == 200):
    response_body = response.read()
    dat = json.loads(response_body.decode('utf-8'))
    late = dat["USD"]["last"]
    symbol = dat["USD"]["symbol"]
    print(late, symbol)
else:
    print("Error Code:" + rescode)
