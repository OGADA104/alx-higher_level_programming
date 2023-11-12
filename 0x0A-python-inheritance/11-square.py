#!/usr/bin/python3
"""square module inheriting from class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inheriting from Rectangle"""

    def __init__(self, size):
        """init class square"""

        self.integer_validator("width", size)
        self.integer_validator("heigth", size)
        self.__size = size

    def area(self):
        """implement area of a sqaure"""

        return self.__size * self.__size

    def __str__(self):
        """implement string formating"""

        return "[Rectangle] {}/{}".format(self.__size, self.__size)
