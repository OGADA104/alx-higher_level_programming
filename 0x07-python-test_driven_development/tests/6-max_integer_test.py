#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    a test class for max_integer
    """

    def test_max(self):
        l_max = max_integer([1, 2, 3, 4])
        self.assertEqual(l_max, 4)
        m_max = max_integer([1, 3, 4, 2])
        self.assertEqual(m_max, 4)


if __name__ == '__main__':
    unittest.main()
