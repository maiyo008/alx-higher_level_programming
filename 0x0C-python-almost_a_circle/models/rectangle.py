#!/usr/bin/python3
# rectangle.py

"""Defines a class that represents a Rectangle"""
from models.base import Base

class Rectangle(Base):
    """Represents a Rectangle"""
    def __init__(self, width,  height, x=0,  y=0, id=None):
        """Intializes every instance of Rectangle

        Args
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): value x
            y (int): value y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width"""
        return (self.__width)
    @property
    def height(self):
        """Returns the height"""
        return (self.__height)
    @property
    def x(self):
        """Returns the x value"""
        return (self.__x)
    @property
    def y(self):
        """Returns the y value"""
        return (self.__y)

    @width.setter
    def width(self, width):
        """Assigns value to the width"""
        self.__width = width
    @height.setter
    def height(self, height):
        """Assigns value to the height"""
        self.__height = height
    @x.setter
    def x(self, x):
        """Assigns value to x"""
        self.__x = x
    @y.setter
    def y(self, y):
        """Assigns value to y"""
        self.__y = y

