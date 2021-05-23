import requests
 
headers = {
    'Accept':  '*/*',
    'User-Agent': 'request'
}
 
url = "https://heroes.free.beeceptor.com/hero"
 
data = {
   "id": 5,
   "name": "Daredevil",
   "age": 33,
   "strength": "super-sense",
   "weakness": "sound-frequency"
}
 
resp = requests.post(url, headers=headers, data=data)
 
print(resp.text)
