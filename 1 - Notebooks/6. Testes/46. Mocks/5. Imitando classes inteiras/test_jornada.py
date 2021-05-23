import unittest
from unittest.mock import patch
import jornada

@patch('jornada.Cubo')
def testa_jornada(mock_cubo):
    class Dado():
        def __init__(self):
            pass

        @property
        def valor(self):
            return 7

        def rolar(self):
            raise ValueError
    
    mock_cubo.return_value = Dado()
    cubo = jornada.Cubo()
    assert cubo.valor == 7
    try:
        cubo.rolar()
    except:
        print("Exceção detectada.")

if __name__ == '__main__':
    unittest.main()
