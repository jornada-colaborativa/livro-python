import unittest
from unittest.mock import Mock
class TestLibraryCommunication(unittest.TestCase):
    def test_send_return_warning(self):
        # Arrange
        mock_email_service = Mock()
        new_library_communication = LibraryCommunication(
            mock_email_service
        )
        # Action
        new_library_communication.send_return_warning("test@mail.com")
        # Assert
        mock_email_service.send_email.assert_called_once_with(
            "test@mail.com",
            "Your loan period ends tomorrow. Please "
            "remember to return or renew your books"
        )
        # o metodo assert_called_once_with() verifica se o metodo do     
        # objeto mock foi chamado apenas uma vez e como a os argumentos 
        # passados. Do contrario levanta uma AssertionError

if __name__ == '__main__':
    unittest.main()
