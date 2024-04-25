#!/usr/bin/python3
"""
This module for task "Rotate 2D Matrix"
"""


def rotate_2d_matrix(matrix):
    """
    This function rotates an n x n 2D matrix 90 degrees clockwise.
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(len(matrix)):
        matrix[i].reverse()
