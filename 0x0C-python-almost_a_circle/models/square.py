#!/usr/bin/python3
"""
This module defines the Square class, a special type of rectangle.

The Square class is defined as a subclass of the Rectangle class from
the models.rectangle module.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, a special type of rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The horizontal position of the square.
        y (int): The vertical position of the square.
        id (int): The identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object.

        Parameters:
            size (int): The size of the square.
            x (int): The horizontal position of the square.
            y (int): The vertical position of the square.
            id (int, optional): The identifier of the square.

        Note:
            The width and height of the square are set to the provided size.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )
