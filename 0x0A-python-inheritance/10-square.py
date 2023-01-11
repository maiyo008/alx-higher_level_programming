#!usr/bin/python3
# 10-square.py

"""Defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class  Square(Rectangle):
    """Represents a Square using Rectangle"""
    def __init__(self, size):
        """Initializes a new square

        Args
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
