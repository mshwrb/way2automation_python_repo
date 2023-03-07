import json

import requests

payload = {
        "name": "zerodha",
        "job": "restricted"
}
response = requests.patch(url="https://reqres.in/api/users/2", data=payload)
print(response.status_code)
print(response.json())
