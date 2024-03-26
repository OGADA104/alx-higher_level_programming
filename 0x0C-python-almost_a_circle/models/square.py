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

    @property
    def size(self):
        """get size if width and height are equal"""
        return self.width

    @size.setter
    def size(self, value):
        """set size """
        self.width = value
        self.height = value
        Rectangle.integer_validator(self, "width", value)
        Rectangle.integer_validator(self, "height", value)

    def update(self, *args, **kwargs):
        """update attributes"""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """save do dict"""
        sq_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }
        return sq_dict
