import requests

def esta_online(url, metodo):
    return requests.__dict__[metodo](url).status_code == 200

def imprime_site(url, metodo='get'):
    if esta_online(url, metodo):
        print(requests.__dict__[metodo](url).text)
