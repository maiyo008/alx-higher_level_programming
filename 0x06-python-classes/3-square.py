#!/usr/bin/python3
# 3-square.py
# tony maiyo
"""Define a Square."""

class Square:
    """Represents a square"""

    def __init__(self, size = 0):
        """Initializes instances of Square

        args
            size(int): The size of the square 

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
