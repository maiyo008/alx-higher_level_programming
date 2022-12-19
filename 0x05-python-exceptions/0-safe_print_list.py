#!/usr/bin/python3
#0-safe_print_list.py

def safe_print_list(my_list = [], x = 0):
    """Function to print x elements of a list"""
    counter = 0
    for i in my_list:
        counter = counter + 1
    try:
        for i in range(x):
            print(my_list[i], end = "")
        print()
        return (x)
    except IndexError:
        print()
        return (counter)
