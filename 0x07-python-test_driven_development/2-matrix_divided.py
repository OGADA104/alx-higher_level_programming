#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    divide a matrix

    args:
        matrix: matrix to be divided
        div: divisor
    return: divided matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    divided_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    return divided_matrix

