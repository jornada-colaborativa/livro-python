import requests
 
headers = {
    'Accept':  '*/*',
    'User-Agent': 'request'
} 

url = "https://heroes.free.beeceptor.com/heroes"
resp = requests.get(url, headers=headers)

print(resp.text)
