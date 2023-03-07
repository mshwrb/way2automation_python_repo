import requests

response = requests.delete(url="https://reqres.in/api/users/2")
print(response)