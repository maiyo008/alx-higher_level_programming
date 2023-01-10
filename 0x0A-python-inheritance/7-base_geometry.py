#!/usr/bin/python3
# 7-base_geometry.py

"""Defines class geometry"""

class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """Function to raise an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validate an integer

        args
            name (string): name of the integer variable
            value (int): the integer value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than  0".format(name))
