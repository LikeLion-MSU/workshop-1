import unittest
from unittest.mock import patch
from io import StringIO
import sys
from basic_calculator import add, sub, mul, div, calculate

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print output
        self.stdout_original = sys.stdout
        self.stdout_capture = StringIO()
        sys.stdout = self.stdout_capture

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.stdout_original

    def assert_output_contains(self, expected_output):
        self.stdout_capture.seek(0)
        output = self.stdout_capture.read()
        self.assertIn(expected_output, output)

    def test_addition(self):
        add(5, 3)
        self.assert_output_contains("5 + 3 = 8")

    def test_subtraction(self):
        sub(10, 3)
        self.assert_output_contains("10 - 3 = 7")

    def test_multiplication(self):
        mul(4, 7)
        self.assert_output_contains("4 * 7 = 28")

    def test_division(self):
        div(15, 3)
        self.assert_output_contains("15 / 3 = 5.0")

if __name__ == '__main__':
    unittest.main()
