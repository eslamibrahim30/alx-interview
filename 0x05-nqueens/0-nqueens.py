#!/usr/bin/python3
"""
This script for task "N queens"
"""
import sys
from typing import List


def inSameDiag(i: List, j: List):
    """
    This method checks if two quens on the same diagonal of the board.
    """
    if i[0] - j[0] == i[1] - j[1] or i[0] + i[1] == j[0] + j[1]:
        return True
    return False


def inSameLine(i: List, j: List):
    """
    This method checks if two quens on the same line of the board.
    """
    if i[0] == j[0] or i[1] == j[1]:
        return True
    return False


def valid_pos(queens: List[List]) -> bool:
    """
    This method checks if the current position is valid solution
    for the N queens problem.
    """
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if inSameDiag(
                queens[i], queens[j]) or inSameLine(
                    queens[i], queens[j]):
                return False
    return True


def list_queen_pos(queens: List[List], n: int) -> list:
    """
    This method for solving the N queens puzzle 
    """
    if len(queens) > n:
        return None
    valid = valid_pos(queens)
    if len(queens) == n and valid:
        print(queens)
        return None
    if not valid:
        return None
    for i in range(n):
        queens.append([queens[-1][0] + 1, i])
        list_queen_pos(queens, n)
        queens.pop()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    n = int(sys.argv[1])
    for i in range(n):
        test_list = [[0, i]]
        test_res = list_queen_pos(test_list, n)
