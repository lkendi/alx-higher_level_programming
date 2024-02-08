#!/usr/bin/python3
"""Module that checks if an object is an instance
of a subclass """


def inherits_from(obj, a_class):
    """Function that checks if an object is an instance
    of a subclass of the specified class

    Args:
        obj(object): object to check
        a_class(class): specified class

    Returns:
        True: if the object is an instance of an indirect or direct
                subclass of a_class
        False: otherwise
    """
    return issubclass(type(obj), a_class) and not type(obj) is a_class
