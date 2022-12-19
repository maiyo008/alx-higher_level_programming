#!/usr/bin/python3
# 100-safe_print_integer_err.py
# Tony Maiyo

import sys


def safe_print_integer_err(value):
    """Function to print an integer

    args:
        value(any type): value parsed to function

    return:
        True if value has been correctly printed
        False if otherwise and prints in stderr error exceeded by exception
    """

    try:
        print("{:d}".format(value))
        ret = True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        ret = False
    return (ret)
