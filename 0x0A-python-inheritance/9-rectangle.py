#!/usr/bin/python3
# 9-rectangle.py

"""Defines a class Rectangle which is a subclass to BaseGeomerty"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using class BaseGeometry"""
    def __init__(self, width, height):
        """Initialize a new Rectangle

        Args
            width (int): width of the rectangle. Greater than zero
            height (int): height of the rectangle. Greater than zero
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the print() and str() of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
