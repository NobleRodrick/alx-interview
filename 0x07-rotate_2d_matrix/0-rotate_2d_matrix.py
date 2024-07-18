#!/usr/bin/python3
"""
function to rotate a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            # The current number
            the_temp = matrix[i][j]
            # changing the top for left
            matrix[i][j] = matrix[x][i]
            # changing the left for bottom
            matrix[x][i] = matrix[y][x]
            # change bottom for right
            matrix[y][x] = matrix[j][y]
            # change right for top
            matrix[j][y] = the_temp
