#!/usr/bin/python3
"""
This module for task "Island Perimeter"
"""


def island_perimeter(grid):
    """
    This function returns the perimeter of the island described in grid.
    """
    i_start = len(grid)
    i_end = 0
    j_start = len(grid)
    j_end = 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
                if i < i_start:
                    i_start = i
                if j < j_start:
                    j_start = j
                if i > i_end:
                    i_end = i
                if j > j_end:
                    j_end = j
    if count == 0:
        return 0
    if count == 1:
        return 1
    return ((j_end - j_start + 1) + (i_end - i_start + 1)) * 2
