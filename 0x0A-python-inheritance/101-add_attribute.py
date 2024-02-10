#!/usr/bin/python3
"""Module that contains a function that can dd a new attribute to a class"""


def add_attribute(obj, att, val):
    """Function that adds a new attribute to an object if possible

    Args:
        obj: object to add attribute to
        att: name of attribute to be added
        val: value of the attribute to be added

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
