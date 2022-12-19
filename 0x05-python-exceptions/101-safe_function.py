#!/usr/bin/python3
# 101-safe_function.py
# Tony Maiyo

import sys


def safe_function(fct, *args):
    """Function to execute a function safely

    args: 
        fct(pointer): pointer to a function

    return:
        result of the function
        None if something happens during function call 
        and print in stderr the error
    """
    try:
        result = fct(*args)
        ret = result
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file = sys.stderr)
        ret = None
    return (ret)
