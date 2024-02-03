#!/usr/bin/python3
"""Matrix multiplication module"""


def matrix_mul(m_a, m_b):
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
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
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

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
