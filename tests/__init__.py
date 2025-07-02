import unittest
from src.utils import factorial

class TestFactorial(unittest.TestCase):

    def test_zero_factorial_should_be_one(self):
            self.assertEqual(factorial(0), 1)

    def test_a_default_number_factorial(self):
        number = 6 # 6! = 24         # Assign
        result = factorial(number)   # Act
        self.assertEqual(result, 720) # Assert
