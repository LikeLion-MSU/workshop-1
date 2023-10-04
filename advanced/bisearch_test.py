import unittest
from binary_search import *

class BinarySearchTests(unittest.TestCase):
    def test_binary_search_found_element(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        element = 6
        result = binary_search(lst, element)
        self.assertEqual(5, result)
        
    def test_binary_search_element_not_in_list(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        element = 11
        result = binary_search(lst, element)
        self.assertEqual(-1, result)

    def test_binary_search_empty_list(self):
        lst = []
        element = 5
        result = binary_search(lst, element)
        self.assertEqual(-1, result)


    def test_binary_search_single_element_list(self):
        lst = [7]
        element = 7
        result = binary_search(lst, element)
        self.assertEqual(0, result)
    
    def test_binary_search_large_list_odd(self):
        lst = [x for x in range(1, 10001)]
        element = 7777
        result = binary_search(lst, element)
        self.assertEqual(7776, result)


