#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary: dictionary
        value: value to look for in dictionary

    Returns:
        The original dictionary with the deleted keys
        Or the original dictionary unchanged if the value does not exist
    """
    keys_to_delete = []
    for key , val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)
        else:
            continue
    for k in keys_to_delete:
        del a_dictionary[k]
    return a_dictionary
