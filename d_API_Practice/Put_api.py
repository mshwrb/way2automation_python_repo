import json

import requests

payload = {
        "name": "Zerodha",
        "job": "Doubly"
}
response = requests.put(url="https://reqres.in/api/users/2", data=payload)
print(response.status_code)
print(response.json())
