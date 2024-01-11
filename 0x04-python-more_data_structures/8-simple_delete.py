#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary
    Assuming that key will always be a string

    Args:
        a_dictionary: the dictionary
        key: key to be deleted from the dictionary

    Returns:
        The dictionary with the specified key deleted
        Or the original dictionary if the key does not exist
    """
    if list is None:
        return
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
