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
        checked = set()
        for i in unchecked:
            if i in unlocked:
                checked.add(i)
                for key in boxes[i]:
                    unlocked.add(key)
        previous_len = len(unchecked)
        unchecked = unchecked.difference(checked)
        current_len = len(unchecked)
        if previous_len == current_len:
            return False
    return True
