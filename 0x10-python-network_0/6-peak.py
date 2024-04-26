#!/usr/bin/python3
"""
Module that contains the function that finds a peak in a list
"""


def find_peak(list_of_integers):
    """Finds a peak in an unsorted list of integers

    Args:
        list_of_integers: unsorte list of integers

    Returns:
        The peak in the list or None
    """

    if len(list_of_integers) <= 1 or list_of_integers is None:
        return None
    else:
        left = 0
        right = len(list_of_integers) - 1

        while (left <= right):
            mid = (left + right) // 2
            if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
                (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
                     return list_of_integers[mid]
            elif (mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]):
                 right = mid - 1
            else:
                 left = mid + 1
