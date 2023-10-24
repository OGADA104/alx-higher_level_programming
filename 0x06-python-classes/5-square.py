#!/usr/bin/python3

"""define class Square."""


class Square:
    """define class Square."""

    def __init__(self, size=0):
        """
        Initializes a square object with a specific size.

        Args:
            size (int): The size (side length) of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """calculate area of square
        Return: area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):

        """retrieve size of square
        Args:
            value (int): new size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):

        """
        print square using #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
