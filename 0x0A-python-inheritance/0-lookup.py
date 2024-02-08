#!/usr/bin/python3
"""Module that list the attributes and methods of an object"""


def lookup(obj):
    """Returns the list of available attributes and methods
    of an object

    Args:
        obj : object to lookup

    Returns:
        list containing attributes and methods of obj
    """
    return dir(obj)
