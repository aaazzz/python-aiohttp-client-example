import requests

url = "http://localhost:7001/api/user/1"

# querystring = {"key1":"value","key2":"value"}

payload = ""
headers = {'x-auth-token': 'hoge'}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
