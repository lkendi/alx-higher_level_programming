#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list

    Args:
        my_list: original list
        search: element to search for and replace in the list
        replace: the new element

    Returns:
        A new list with the elements replaced
    """
    new_list = list()
    for item in my_list:
        new_list.append(replace if item == search else item)
    return new_list
