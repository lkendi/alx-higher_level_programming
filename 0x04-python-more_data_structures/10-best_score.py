#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value
    Assuming that all values are only integers
    And all stdents have a different score

    Args:
        a_dictionary: the dictionary

    Returns:
        The key with the biggest integer value
        None if no score is found
    """
    max_key = None
    max_val = 0
    if a_dictionary is None:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > max_val:
                max_key = key
                max_val = value
        return max_key
