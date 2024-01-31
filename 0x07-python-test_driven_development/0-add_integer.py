#!/usr/bin/python3
"""
Module that contains a function to add 2 integers
"""


def add_integer(a, b=98):
    """Function that adds 2 integers

    Args:
        a (int): first integer
        b (int, optional): second integer (default value of 98)

    Returns:
        int: sum of the 2 integers

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
