#!/usr/bin/python3
"""
This module for task "Prime Game"
"""

def countTurns(n):
    prime = [True for i in range(n+1)]
    turns = 0
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            turns += 1
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return turns

def isWinner(x, nums):
    """
    This function returns the name of the player that won the most rounds.
    """
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
    return 'Ben'