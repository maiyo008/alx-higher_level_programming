#!/usr/bin/python3
# base.py

"""Define a Base class for all other classes in this project"""

class Base():
    """Represents Base class"""
    __nb_objects = 0
    
    def __init__(self, id = None):
        """Initializes every instance of Base class

        Args
            id (int): ID value representing every instance created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
