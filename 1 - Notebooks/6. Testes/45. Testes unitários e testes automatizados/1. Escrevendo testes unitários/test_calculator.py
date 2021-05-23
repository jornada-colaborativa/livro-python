import unittest
from calculator import Calculator
class CalculatorTest(unittest.TestCase):
    def test_pow_positive_exponent(self):
        # teste unitario do modulo pow
        # Arrange
        calculator = Calculator()
        # Action
        result = calculator.pow(2, 3)
        # Assert
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
