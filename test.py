#!/usr/bin/python3
import unittest
from multiply import multiply

class TestSum(unittest.TestCase):
    def test_1(self):
        result1 = multiply(10, 5)
        self.assertEqual(result1, 50)
    def test_2(self):
        result2 = multiply(20, 0)
        self.assertEqual(result2, 0)
    def test_3(self):
        result3 = multiply(15, 10)
        self.assertEqual(result3, 150)


if __name__ == '__main__':
    unittest.main()
