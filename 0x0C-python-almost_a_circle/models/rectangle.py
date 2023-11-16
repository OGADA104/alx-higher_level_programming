#!/usr/bin/python3
"""
    first rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """class rectangle created"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method """
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

    def __str__(self):
        """format printing"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """get area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """displat the rectangle"""
        for y in range(self.__y):
            print()

        for i in range(self.__height):
            for x in range(self.__y):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """update attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
