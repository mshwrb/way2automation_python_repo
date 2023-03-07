import requests

# # This will give The read operation timed out error because of timeout lower than what passed as path params in request
# response = requests.get("https://httpbin.org/delay/3", timeout=1)
# print(response.status_code)

# This will return the response with in the 4 seconds
response = requests.get("https://httpbin.org/delay/3", timeout=4)
print(response.status_code)
