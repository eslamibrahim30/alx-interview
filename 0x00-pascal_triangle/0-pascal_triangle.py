#!/usr/bin/python3
"""This module is an implementation for
Pascal's Triangle generator function"""


def pascal_triangle(n):
    """ This funciton generates Pascal's Triangle"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        pascal_tri = list()
        pascal_tri.append(list([1]))
        for i in range(1, n):
            current_row = list()
            current_row.append(1)
            for j in range(1, len(pascal_tri[-1])):
                current_row.append(pascal_tri[-1][j] + pascal_tri[-1][j - 1])
            current_row.append(1)
            pascal_tri.append(current_row)
        return pascal_tri
