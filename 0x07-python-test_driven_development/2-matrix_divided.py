#!/usr/bin/python3
"""
Matrix division module
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix

    Args:
        matrix(list): matrix input
        div (int/float): divisor

    Raises:
        TypeError: if matrix is not a list of list of integers or floats
                    or if each matrix row is not of the same size
                    or if div is not a number
        ZeroDivisionError: if div == 0

    Returns:
        A new matrix with all matrix elements divided by div
        and rounded to 2 decimal places
    """
    if not all(isinstance(row, list) and
               all(isinstance(element, (int, float)) for element in row)
               for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(value/div, 2) for value in row] for row in matrix]
    return result
