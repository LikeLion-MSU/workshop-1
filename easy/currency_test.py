import unittest
from currency_converter import *

class TestConvertFunction(unittest.TestCase):

    def test_convert_positive_dollars(self):
        result = convert(100)
        expected_result = "This program converts US dollars to Korean Won\n$100 is 135662.0 won"
        self.assertEqual(result, expected_result)

    def test_convert_zero_dollars(self):
        result = convert(0)
        expected_result = "This program converts US dollars to Korean Won\n$0 is 0.0 won"
        self.assertEqual(result, expected_result)

    def test_convert_negative_dollars(self):
        result = convert(-50)
        expected_result = "Cannot have negative value"
        self.assertEqual(result, expected_result)

    def test_convert_large_amount(self):
        result = convert(1000000)
        expected_result = "This program converts US dollars to Korean Won\n$1000000 is 1356620000.0 won"
        self.assertEqual(result, expected_result)

    def test_convert_float_dollars(self):
        result = convert(75.5)
        expected_result = "This program converts US dollars to Korean Won\n$75.5 is 102424.81 won"
        print(result)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
