import requests

baseurl = 'https://wallhaven.cc/api/v1/w/'
endpoint = '94x38z'
url = baseurl + endpoint
print (url)
response = requests.get(url)

print(response)