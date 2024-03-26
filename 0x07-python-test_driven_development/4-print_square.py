#!/usr/bin/python3
""" print squares"""


def print_square(size):
    """
     Print a square of '#' characters.

     Args:
        size (int): The size of the square.
    Raises:
        TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
    """
    if size < 0:
        print()
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
