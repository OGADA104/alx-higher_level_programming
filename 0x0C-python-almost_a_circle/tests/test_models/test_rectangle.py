#!/usr/bin/python3
""" test module for class rectangle"""

import unittest
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    """test case class"""

    def setUp(self):
        """set up r1 and r2"""
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        """clean up instances"""
        del self.r1
        del self.r2
        del self.r3

    def test_id(self):
        """test for id"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)

    def test_RaiseError(self):
        """test for error raised"""
        with self.assertRaises(ValueError):
            self.r1.width = -10

    def test_area(self):
        """test for area """
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 20)

    def test_update(self):
        """test for updates"""
        self.r1.update(89)
        self.assertEqual(self.r1.id, 89)
        self.r2.update(89, 2, 3)
        self.assertEqual(self.r2.width, 2)
        self.r1.update(height=4)
        self.assertEqual(self.r1.height, 4)

if __name__ == '__main__':
    unittest.main()
