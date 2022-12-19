#!/usr/bin/python3
#1-safe_print_integer.py

def safe_print_integer(value):
    """A function that prints an integer 

    args:
        value : an input value of any type

    return:
        True if value has been printed successfully
        False if otherwise
        """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
