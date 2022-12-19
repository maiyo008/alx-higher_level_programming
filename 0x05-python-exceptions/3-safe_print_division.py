#!/usr/bin/python3
#3-safe_print_division.py

def safe_print_division(a, b):
    """Function that divides 2 ints and prints results

    args:
        a: First integer
        b: Second integer

    return:
        Value of division
        Otherwise none
    """
    quotient = 0
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return (quotient)
