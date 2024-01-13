#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple

    Args:
        my_list - list of tuples (<score>, <weight>)

    Returns:
        weighted average
    """
    if my_list is None or len(my_list) == 0:
        return 0
    result = 0
    weight_sum = 0
    for score, weight in my_list:
        result += score * weight
        weight_sum += weight
    return (result/weight_sum)
