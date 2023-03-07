import requests

params = {"page": 2}
response = requests.get(url="https://reqres.in/api/users", params=params)
# response = requests.request(method="GET", url=url, params=, data= ,headers=, files=, auth=,timeout=,allow_redirects=,proxies=,hooks=,stream=,verify=,cert=,json=)

response_text = response.text
response_json = response.json()
response_content = response.content
status_code = response.status_code
response_headers = response.headers
response_encoding = response.encoding
response_cookies = response.cookies
response_url = response.url

# return response status code in the format <class 'int'>
print(status_code)
print(type(response.status_code))

# return response in plain string format <class 'str'>
print(response_text)
print(type(response_text))

# return response in byte format <class 'bytes'>
print(response_content)
print(type(response_content))

# return response in json serialize format <class 'dict'>
print(response_json)
print(type(response_json))

# return headers in response <class 'requests.structures.CaseInsensitiveDict'>
print(response_headers)
print(type(response_headers))

# return encoding embedded by api, in this case utf-8 with type <class 'str'>
print(response_encoding)
print(type(response_encoding))

# return cookies jar with class type 'requests.cookies.RequestsCookieJar'>
print(response_cookies)
print(type(response_cookies))

# return cookies jar with class type 'requests.cookies.RequestsCookieJar'>
print(response_url)
print(type(response_url))

# accessing data from response
print(response_json['total_pages'])
print(response_json['total'])

for n in response_json["data"]:
    print(n)

print(
    "----------------------------------------------------------------------------------------------------------------------------------------------------------")
print(response_json["data"][0])
print(response_json["data"][0]["id"])

print(response_json["data"][0]["email"])
assert (response_json["data"][0]["email"]).endswith("reqres.in"), "email format is not matching"

print(response_json["support"]["url"])
