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
    if my_list is None or len(my_list) <= 0:
        return
    else:
        new_list = my_list.copy()
        for idx in range(0, len(new_list)):
            if new_list[idx] == search:
                new_list[idx] = replace
        return new_list
