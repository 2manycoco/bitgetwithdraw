import time
import hmac
import hashlib
import requests
import json

apiKey = 'BITGET_API_KEY'
secret = 'BITGET_SECRET'
passphrase = 'BITGET_PASSPHRASE'

timestamp = str(int(time.time() * 1000))
coin = "USDT"
amount = "10"
network = "TRC20"
address = "YOUR_WHITELISTED_ADDRESS"
clientOid = timestamp

# Create signature
body = {
    "coin": coin,
    "address": address,
    "chain": network,
    "amount": amount,
    "clientOid": clientOid
}

sign_str = timestamp + apiKey + json.dumps(body)
signature = hmac.new(secret.encode(), sign_str.encode(), hashlib.sha256).hexdigest()

headers = {
    "ACCESS-KEY": apiKey,
    "ACCESS-SIGN": signature,
    "ACCESS-TIMESTAMP": timestamp,
    "ACCESS-PASSPHRASE": passphrase,
    "Content-Type": "application/json"
}

url = "https://api.bitget.com/api/v2/spot/wallet/withdrawal"
response = requests.post(url, headers=headers, json=body)
print("Bitget withdrawal:", response.json())
