#!/usr/bin/python3
#4-list_division.py

def list_division(my_list_1, my_list_2, list_length):
    """Function to divide element by element 2 lists

    args:
        my_list_1: first list
        my_list_2: second list
        list_length: length of the list and can be bigger than both lists

    return:
        a new list of length equal to list_length with all divisions
    """
    quotient_list = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("Out of range")
            quotient = 0
        finally:
            quotient_list.append(quotient)
    return (quotient_list)
