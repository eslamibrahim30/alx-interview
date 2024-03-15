#!/usr/bin/python3
"""
This module is for task "Lockboxes"
"""


def canUnlockAll(boxes):
    """
    This funciton determines if all the boxes can be unlocked
    """
    unlocked = set()
    unlocked.add(0)
    unchecked = set(range(len(boxes)))
    while len(unlocked) != len(boxes):
        prev_unlocked = len(unlocked)
        prev_unchecked = len(unchecked)
        checked = set()
        for i in unchecked:
            if i in unlocked:
                checked.add(i)
                for key in boxes[i]:
                    unlocked.add(key)
        unchecked = unchecked.difference(checked)
        cur_unlocked = len(unlocked)
        cur_unchecked = len(unchecked)
        if cur_unlocked == prev_unlocked and cur_unchecked == prev_unchecked:
            return False
    return True
