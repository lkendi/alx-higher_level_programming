#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary will all values multiplied by 2
    Assuming that all values are only integers

    Args:
        a_dictionary - original dictionary

    Returns:
        a new dictionary with all values of the original dictionary
        multiplied by 2
        """
    return {key: value * 2 for key, value in a_dictionary.items()}
