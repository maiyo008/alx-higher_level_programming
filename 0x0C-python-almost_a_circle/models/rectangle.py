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
        """Assigns value to the width

        args
            width (int): value of the width
        Raises
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width
    @height.setter
    def height(self, height):
        """Assigns value to the height

        Args
            height (int): value of the height
        Raises
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height
    @x.setter
    def x(self, x):
        """Assigns value to x

        Args
            x (int): value for x
        Raises
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x
    @y.setter
    def y(self, y):
        """Assigns value to y

        Args
            y (int): value for y
        Raises
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y
    def area(self):
        """Returns the value of the area instance of a rectangle"""
        return (self.__width * self.__height)
    def display(self):
        """Prints the rectangle with the # character"""
        for  y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()
    def __str__(self):
        """Print the rectangle parameters"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) +  ") "
        string += str(self.__x) + "/" + str(self.__y)
        string += " - " + str(self.__width) + "/" + str(self.__height)
        return (string)
    def update(self, *args):
        """Update the parameters of Rectangle

        Args
            args[0]: id
            args[1]: width
            args[2]: height
            args[3]: x
            args[4]: y
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
