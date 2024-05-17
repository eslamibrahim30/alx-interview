#!/usr/bin/python3
"""
This module for task "Prime Game"
"""


def countTurns(n):
    """
    This function returns the number of rest turns of the round
    based on given number.
    """
    prime = [True for _ in range(n+1)]
    turns = 0
    p = 2
    while (p <= n):
        if (prime[p] is True):
            turns += 1
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return turns


def isWinner(x, nums):
    """
    This function returns the name of the player that won the most rounds.
    """
    if not nums or x < 1:
        return None
    p1 = 0
    p2 = 0
    for round in range(x):
        turns = countTurns(nums[round])
        if turns % 2 == 0:
            p2 += 1
        else:
            p1 += 1
    if p1 > p2:
        return 'Maria'
    elif p2 > p1:
        return 'Ben'
    return None
