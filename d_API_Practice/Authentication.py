import requests
from requests.auth import HTTPBasicAuth

# # Basic Authentication
# username = "admin"
# password = "admin"
# response = requests.get(url="https://the-internet.herokuapp.com/basic_auth",
#                         auth=HTTPBasicAuth(username=username, password=password))
# print(response.status_code)

# [Basic Authentication]
response_1 = requests.get(url="https://restapi.demoqa.com/authentication/CheckForAuthentication")
print(response_1.status_code)

