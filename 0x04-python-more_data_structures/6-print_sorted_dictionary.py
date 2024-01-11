#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary ordered by keys
    Assuming that all keys are strings

    Args:
        a_dictionary: the dictionary

    Returns:
        The dictionary ordered by keys
    """
    for key in sorted(a_dictionary.keys()):
        print(key, ":", a_dictionary[key])
