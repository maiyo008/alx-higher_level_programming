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
        return self.width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    def update(self, *args, **kwargs):
        """ Function to update square parameters

        Args
            *args (ints); New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if  a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y,self.id)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a ==  3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k ==  "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
