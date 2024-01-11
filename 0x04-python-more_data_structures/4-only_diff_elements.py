#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set containing elements present in only one of the 2 sets

    Args:
    set_1: first set
    set_2: second set

    Returns:
        A set containing elements present in only one of the sets
 """
    return (set_1.difference(set_2)).union(set_2.difference(set_1))
