#!/usr/bin/python3
""" base class test module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        """setup tests"""

        self.b1 = Base()
        self.b2 = Base(99)
        self.b3 = Base()
        self.b4 = Base(-123)

    def test_Id(self):
        """run tests"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 99)
        self.assertEqual(self.b4.id, -123)
        self.assertEqual(self.b3.id, 2)


if __name__ == '__main__':
    """run test file as main"""
    unittest.main()
