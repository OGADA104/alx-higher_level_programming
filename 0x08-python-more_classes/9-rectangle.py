#!/usr/bin/python3
""" Define  class rectangle """


class Rectangle:
    """
    an empty class rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def Rectangle_instances(self):
        """
        get number of instances
        """
        return Rectangle.number_of_instances

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
            rectangle_str += str(Rectangle.print_symbol) * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """
        return string reprentstion of instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        deletion of a reectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method to compare rectangles
        args:
            rect_1: first rectangle
            rect_2: second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        a class method to create a square
        """
        if size > 0:
            new_rect = cls(size, size)
            return new_rect
