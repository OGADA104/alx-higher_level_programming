#!/usr/bin/python3
""" Define  class rectangle """


class Rectangle:
    """
    an empty class rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """set witdth to  value
        args:
            value: new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height
        args:
            value: new height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        get area of rectangle
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ get perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """
        print rectangle with # character
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for x in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()
