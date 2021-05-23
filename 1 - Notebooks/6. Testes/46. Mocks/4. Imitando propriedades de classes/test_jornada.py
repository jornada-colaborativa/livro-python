import unittest
from unittest.mock import patch
from unittest.mock import PropertyMock
from jornada import Jornada

@patch('jornada.Jornada.nome', new_callable=PropertyMock)
def testa_jornada(mock_property):
    jornada = Jornada('Jupiter')
    print(jornada.nome)
    mock_property.assert_called()
    jornada.nome = 'Zeus'
    mock_property.assert_called()
    print(jornada.nome)
    mock_property.assert_called()

if __name__ == '__main__':
    unittest.main()
