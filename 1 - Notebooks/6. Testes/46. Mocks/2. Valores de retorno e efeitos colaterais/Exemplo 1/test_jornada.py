import unittest
from unittest.mock import patch
from jornada import imprime_site

@patch('jornada.esta_online', return_value=False)
@patch('jornada.requests.post')
@patch('jornada.requests.get')
def testa_imprime_site(mock_get, mock_post, mock_online):
    imprime_site('http://httpbin.org/get')
    mock_get.assert_not_called()
    imprime_site('http://httpbin.org/post', 'post')
    mock_post.assert_not_called()
    mock_online.assert_called()

if __name__ == '__main__':
    unittest.main()
