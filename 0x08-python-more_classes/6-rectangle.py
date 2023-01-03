#!/usr/bin/python3
# 6-rectangle.py
# Tony  Maiyo

"""Defines a class Rectangle"""

class Rectangle:
    """Represents a rectangle

    Attributes:
        number_of_instances(int): The number of Rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width = 0, height = 0):
        """Initialize a  new rectangle.

        Args:
            width(int): The size of width of the square
            height(int): The size of the height of the square
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self): 
        """Gets the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)
    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Return the printable representation of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
