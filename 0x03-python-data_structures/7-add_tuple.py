#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    add_tuple - adds corresponding elements of 2 tuples
    
    Args:
        tuple_a: first tuple
        tuple_b: second_tuple
    
    Returns:
        final tuple with the sum of corresponding elements
    """
    if len(tuple_a) < 2:
        tuple_a += (0, ) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0, ) * (2 - len(tuple_b))

    final_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return final_tuple
