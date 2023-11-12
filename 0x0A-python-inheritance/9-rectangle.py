#!/usr/bin/python3
"""Rectangle module inheriting from base class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle inheriting from base"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """calculate area of rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """implement print """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
