#!/usr/bin/python3
"""Module that checks if an object is an instance of a class
or its subclasses"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of a class
    or its subclasses

    Args:
        obj (object): object to check
        a_class (class): specified class

    Returns:
        True: if obj is an instance of a_class or of its subclass
        False: otherwise
    """
    return isinstance(obj, a_class)
