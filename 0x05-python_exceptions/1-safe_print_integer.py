#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer, handling potential errors.

    Args:
        value: if integer, integer to print using "{:d}".format()"
        value can be any type (integer, string, etc.)

    Returns:
        True if value has been correctly printed (it means the value is an integer)
        Otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
