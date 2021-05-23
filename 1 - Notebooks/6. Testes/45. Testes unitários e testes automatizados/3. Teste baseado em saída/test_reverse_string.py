import unittest
from reverse_string import reverse_string
class TestReversestring(unittest.TestCase):
    def test_reverse_string_not_empty_string(self):
        # Arrange
        string = "onibus"
        # Action
        result = reverse_string(string)
        # Assert
        self.assertEqual(result, "subino")

if __name__ == '__main__':
    unittest.main()
