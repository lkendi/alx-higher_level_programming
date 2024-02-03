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

    Returns:
        numpy array: result of matrix multiplication
    """
    np_a = np.array(m_a)
    np_b = np.array(m_b)
    result = np.matmul(np_a, np_b)
    return result
