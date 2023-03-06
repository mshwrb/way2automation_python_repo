import requests

response = requests.get("https://reqres.in/api/users?page=2")
status_code = response.status_code
print(status_code)
print(response.text)
print(response.content)
print(response.json())
