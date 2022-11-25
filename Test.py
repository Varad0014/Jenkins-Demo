#!/usr/bin/python3
# Test case for multiplication two numbers
import unittest

from Program import multiply

class TestMultiply(unittest.TestCase):
    def test1(self):
        data = [40, 80]
        result = multiply(data)
        self.assertEqual(result, 3200)

    def test2(self):
        data = [24, 2]
        result = multiply(data)
        self.assertEqual(result, 48)

    def test3(self):
        data = [50, 2]
        result = multiply(data)
        self.assertEqual(result, 100)

    def test4(self):
        data = [16, 8]
        result = multiply(data)
        self.assertEqual(result, 48)

    def test5(self):
        data = [6, 8]
        result = multiply(data)
        self.assertEqual(result, 72)

if __name__ == '__main__':
    unittest.main()