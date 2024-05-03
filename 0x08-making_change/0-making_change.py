#!/usr/bin/python3
"""
This module for task "Change comes from within"
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Given a pile of coins of different values. This function determine
    the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num = 0
    for i in coins:
        num += total // i
        total %= i
    if total != 0:
        return -1
    return num
