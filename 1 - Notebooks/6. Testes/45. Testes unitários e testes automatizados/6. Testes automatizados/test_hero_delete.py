import requests
 
headers = {
    'Accept':  '*/*',
    'User-Agent': 'request'
}
 
url = "https://heroes.free.beeceptor.com/hero/1"
resp = requests.delete(url, headers=headers)
 
print(resp.text)
