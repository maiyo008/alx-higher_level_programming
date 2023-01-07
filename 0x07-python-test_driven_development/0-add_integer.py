#!/usr/bin/python3
# 0-add_integer.py
# Tony Maiyo

def add_integer(a,  b = 98):
    """ Return an integer that is the sum of a and b
    
    Typecast floats to ints before addition

    Raises:
        TypeError: if either a or b is a non-integer and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError(" b  must be an integer")
    return (int(a) + int(b))
