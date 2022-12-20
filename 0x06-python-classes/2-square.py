#!/usr/bin/python3
# 2-square.py
# Tony Maiyo
"""Define a class Square"""

class Square:
    """Represents a square."""

    def __init__(self, size = 0):
        """ Initializes every instance of Square

        args
            size(int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
