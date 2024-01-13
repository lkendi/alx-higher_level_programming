#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """
    Computes the square of all integers of a matrix using map
    
    Args:
        matrix - matrix of integers
    
    Returns:
        square value of all integers of the matrix
    """
    return list(map(lambda row: list(map(lambda num: num **2, row)), matrix))
