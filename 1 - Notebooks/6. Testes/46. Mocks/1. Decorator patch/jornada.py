import requests

def imprime_site(url, metodo='get'):
    response = requests.__dict__[metodo](url)
    if response.status_code == 200:
        print(response.text)
