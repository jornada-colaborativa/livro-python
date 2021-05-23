import unittest
from unittest.mock import patch
from jornada import imprime_site

@patch('jornada.requests.post')
@patch('jornada.requests.get')
def testa_imprime_site(mock_get, mock_post):
    imprime_site('http://httpbin.org/get')
    mock_get.assert_called()

    imprime_site('http://httpbin.org/post', 'post')
    mock_post.assert_called()

if __name__ == '__main__':
    unittest.main()
