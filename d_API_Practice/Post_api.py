import json
import requests

payload = open("z_payload.json", "r").read()

response = requests.post(url="https://reqres.in/api/users", data=json.loads(payload))
print(response.status_code)
print(response.json())


payload_1 = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response_1 = requests.post(url="https://reqres.in/api/register", data=payload_1)
print(response_1.status_code)
print(response_1.json())

