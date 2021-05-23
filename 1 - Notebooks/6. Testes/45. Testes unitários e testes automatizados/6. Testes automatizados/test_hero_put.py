import requests
 
headers = {
    'Accept':  '*/*',
    'User-Agent': 'request'
}
 
url = "https://heroes.free.beeceptor.com/hero/4"
 
data = {
   "id": 4,
   "name": "Captain Marvel",
   "age": 27,
   "strength": "phisical-strength",
   "weakness": "diseases"
}
 
resp = requests.put(url, headers=headers, data=data)
 
print(resp.text)
