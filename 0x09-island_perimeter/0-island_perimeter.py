#!/usr/bin/python3
"""
This module for task "Island Perimeter"
"""


def island_perimeter(grid):
    """
    This function returns the perimeter of the island described in grid.
    """
    if not isinstance(grid, list):
        return 0
    perm = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perm += 4
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    perm -= 2
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    perm -= 2
    return perm
