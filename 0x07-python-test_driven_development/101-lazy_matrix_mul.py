#!/usr/bin/python3
"""
Matrix multiplication using numpy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices

    Args:
        m_a: first matrix
        m_b: second matrix

    Raises:
        TypeError: if m_a or m_b is not a list of lists
                   or if any of the elements is not an int or float
                   or if m_a or m_b is not a rectangle
                   (all rows with the same size)
        ValueError: if m_a or m_b is empty
                   or if m_a and m_b can't be multiplied
    Returns:
        numpy array: result of matrix multiplication
    """
    if not isinstance(m_a, list) or not all(
            isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(
            isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(value, (int, float))
               for row in m_a for value in row):
        raise ValueError(
                        "m_a should contain only integers or floats")
    if not all(isinstance(value, (int, float))
               for row in m_b for value in row):
        raise ValueError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    np_a = np.array(m_a)
    np_b = np.array(m_b)
    result = np.matmul(np_a, np_b)
    return result.tolist()
