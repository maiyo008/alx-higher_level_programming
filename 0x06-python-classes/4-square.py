#!/usr/bin/python3
# 4-square.py
# tony maiyo
"""Define a Square."""

class Square:
    """Represents a square"""

    def __init__(self, size = 0):
        """Initializes instances of Square

        args
            size(int): The size of the square 

        """
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
    
    @property
    def size(self):
        """Retreives the attribute size"""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """Sets the attribute size

        args
            value(int): The value to modify the size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
