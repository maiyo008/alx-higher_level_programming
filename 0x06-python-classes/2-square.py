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
        try:
            if (size < 0):
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
