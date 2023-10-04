import unittest
from leap_year_checker import *

class TestLeapYear(unittest.TestCase):

    def test_leap_year_divisible_by_4(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2024))
        self.assertTrue(is_leap_year(1996))

    def test_leap_year_divisible_by_100(self):
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertFalse(is_leap_year(2200))

    def test_leap_year_divisible_by_400(self):
        self.assertTrue(is_leap_year(1600))
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2400))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(2022))
        self.assertFalse(is_leap_year(2101))
        self.assertFalse(is_leap_year(2202))

    def test_negative_year(self):
        self.assertFalse(is_leap_year(-2000))
        self.assertFalse(is_leap_year(-2024))
        self.assertFalse(is_leap_year(-1996))

if __name__ == '__main__':
    unittest.main()
