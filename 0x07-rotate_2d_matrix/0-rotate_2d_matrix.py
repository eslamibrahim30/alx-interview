#!/usr/bin/python3
"""
This module for task "Rotate 2D Matrix"
"""
from typing import List


def rotate_2d_matrix(matrix: List[List]) -> None:
    """
    This function rotates an n x n 2D matrix 90 degrees clockwise.
    """
    rotated_mat = [
        [matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))
    ]
    for i in range(len(rotated_mat)):
        rotated_mat[i].reverse()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = rotated_mat[i][j]
