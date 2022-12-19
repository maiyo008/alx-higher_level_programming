#!/usr/bin/python3
#2-safe_print_list_integers.py

def safe_print_list_integers(my_list = [], x = 0):
    """Function to print the first x elements of integers in a list

    args:
        my_list: List to provide the elements to be printed
        x: number of elements to access in my_list

    return:
        The real number of integers printed
    """
    counter = 0;
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end = "")
            counter = counter + 1;
        except (TypeError, ValueError):
            continue
    print("")
    return (counter)
