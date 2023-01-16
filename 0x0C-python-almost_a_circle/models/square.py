#!/usr/bin/python3
# square.py

"""Defines class Square"""

from  models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a Square that inherits from a Rectangle.

    A square is a rectangle with equal height and width
    """
    def __init__(self, size, x = 0, y = 0,  id=None):
        """Initializes every instance of the Square

        Args
            size (int): the width of height of the square
            x (int): the x cordinate 
            y (int): the y cordinate
            id (int): the identity of the new square
        """
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        """Returns the size of the square"""
        return self.size
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
