#!/usr/bin/python3
"""first rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class rectangle created"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.__width = value
        self.integer_validator("width", value)

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set new height"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set new value for x"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set new value for y"""
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Validate integer values"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name in ("width", "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ("x", "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def __str__():
        """format printing"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
