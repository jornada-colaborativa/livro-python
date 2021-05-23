import numpy as np

class Cubo():
    def __init__(self):
        self.__valor = np.random.randint(1, 6)
    
    @property
    def valor(self):
        return self.__valor
    
    def rolar(self):
        self.__valor = np.random.randint(1, 6)
