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
