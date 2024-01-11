#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Returns a new matrix with the sqaure of each corresponding element
    without modifying the original matrix

    Args:
        matrix: A list of lists which is the matrix

    Returns:
        A new list of lists with each element of the original matrix sqaured
        """
    return [[num ** 2 for num in row] for row in matrix]
