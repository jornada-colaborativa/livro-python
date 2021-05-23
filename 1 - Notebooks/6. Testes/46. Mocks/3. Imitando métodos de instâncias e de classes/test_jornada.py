import unittest
from unittest.mock import patch
from jornada import Jornada

@patch('jornada.Jornada.esta_online', return_value=True)
def testa_imprime_site(mock_online):
    jornada = Jornada()
    jornada.imprime_site('http://httpbin.org/post', 'post')
    mock_online.assert_called()
    mock_online.reset_mock()

    with patch('jornada.Jornada.esta_online', 
    return_value=True) as mock_method:
        jornada.imprime_site('http://httpbin.org/get', 'get')
        mock_method.assert_called()
        mock_method.reset_mock()
    
    with patch.object(Jornada, 'esta_online', 
    return_value=True) as mock_obj:
        jornada.imprime_site('http://httpbin.org/get', 'get')
        mock_obj.assert_called()
        mock_obj.reset_mock()

if __name__ == '__main__':
    unittest.main()
