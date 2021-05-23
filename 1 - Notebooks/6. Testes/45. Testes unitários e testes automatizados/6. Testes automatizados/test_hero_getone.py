import requests
 
headers = {
    'Accept':  '*/*',
    'User-Agent': 'request'
} 

url = "https://heroes.free.beeceptor.com/hero/4"

resp = requests.get(url, headers=headers)

print(resp.text)
