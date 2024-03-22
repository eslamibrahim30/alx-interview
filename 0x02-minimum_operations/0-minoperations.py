#!/usr/bin/python3
"""
This module is for task "Minimum Operations"
"""


def minOperations(n):
    """
    This function calculates the fewest number of Copy All and Paste
    needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    current_div = n
    steps = 0
    while current_div > 1:
        for i in range(int(current_div / 2), 0, -1):
            if current_div % i == 0:
                steps += int(current_div / i)
                current_div = i
                break
    return steps
