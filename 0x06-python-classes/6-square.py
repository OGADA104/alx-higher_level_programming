#!/usr/bin/python3

"""define class Square."""


class Square:
    """define class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square object with a specific size.

        Args:
            size (int): The size (side length) of the square.
            position (int): position of
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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

    @property
    def position(self):
        """
        retrieve position

        Returns:
            position
        """
        return self.__position

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

    @position.setter
    def position(self, value):

        """
        set position
        Args:
            value (int): new value for position
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):

        """
        print square using #
        """
        x, y = self.__position
        for _ in range(y):
            print()
        for _ in range(self.__size):
            print(" " * x + "#" * self.__size)
