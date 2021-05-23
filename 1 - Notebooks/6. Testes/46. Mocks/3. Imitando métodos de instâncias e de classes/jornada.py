import requests

class Jornada():
    def __init__(self):
        pass

    def esta_online(self, url, metodo):
        return requests.__dict__[metodo](url).status_code == 200

    def imprime_site(self, url, metodo='get'):
        try:
            if self.esta_online(url, metodo):
                print(requests.__dict__[metodo](url).text)
        except Exception:
            print("Exceção detectada.")
