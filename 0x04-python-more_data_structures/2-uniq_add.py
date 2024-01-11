#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer)

    Args:
        my_list: list of integers

    Returns:
        Result of the addition
    """
    return (sum(set(my_list)))
