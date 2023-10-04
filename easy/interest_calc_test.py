import unittest
from interest_calculator import interest_calculator

class TestInterestCalculator(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(interest_calculator(1000, 5.0, 5), " The monthly payment for this loan is: 18.87 ")
    
    def test_zero_principal(self):
        self.assertEqual(interest_calculator(0, 5.0, 5), " The monthly payment for this loan is: 0.00 ")
    
    def test_zero_apr(self):
        self.assertEqual(interest_calculator(1000, 0, 5), " The monthly payment for this loan is: 0.00 ")
    
    def test_zero_years(self):
        self.assertEqual(interest_calculator(1000, 5.0, 0), " The monthly payment for this loan is: 0.00 ")
    
    def test_negative_principal(self):
        self.assertEqual(interest_calculator(-1000, 5.0, 5), " The monthly payment for this loan is: 0.00 ")

if __name__ == '__main__':
    unittest.main()
