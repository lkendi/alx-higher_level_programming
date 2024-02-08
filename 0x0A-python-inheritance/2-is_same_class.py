#!/usr/bin/python3
"""Module that checks if an object is an instance of a secified class"""


def is_same_class(obj, a_class):
    """Funcion that checks if an object is exactly an
    instance of the specified class

    Args:
        obj (object): object to check
        a_class (class): check whetther obj is an instnace of this class

    Returns:
        True: if the object is exactly an instance of the specified class
        False: otherwise
    """
    return type(obj) is a_class
