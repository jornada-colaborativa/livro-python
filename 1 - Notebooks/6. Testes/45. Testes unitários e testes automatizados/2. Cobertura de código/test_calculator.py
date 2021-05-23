import unittest
from calculator import Calculator
class CalculatorTest(unittest.TestCase):
    # testes unitarios do modulo pow
    def test_pow_positive_exponent(self):
        # Arrange
        calculator = Calculator()
        # Action
        result = calculator.pow(2, 3)
        # Assert
        self.assertEqual(result, 8)

    def test_pow_negative_exponent(self):
        # Arrange
        calculator = Calculator()
        # Action/Assert
        with self.assertRaises(ValueError):
            calculator.pow(2, -2)
    
    def test_pow_zero_exponent(self):
        # Arrange
        calculator = Calculator()
        # Action
        result = calculator.pow(2, 0)
        # Assert
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
