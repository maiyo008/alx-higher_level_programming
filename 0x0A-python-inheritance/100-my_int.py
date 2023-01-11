#!/usr/bin/python3
# 100-my_int.py

"""Defines MyInt class that inherits from int"""

class MyInt(int):
    """Invert the functionality of == and != operators"""
    def __eq__(self, value):
        """Override == operator with !="""
        return (self.real != value)
    def __ne__(self, value):
        """Override the != operator with =="""
        return (self.real != value)
