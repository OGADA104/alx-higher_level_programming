#!/usr/bin/python3
"""basegeometry class"""


class BaseGeometry:
    """my empty baseGeometry class"""

    def area(self):
        """get area of my geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate integer input"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
