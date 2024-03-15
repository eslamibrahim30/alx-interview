#!/usr/bin/python3
"""
This module is for task "Lockboxes"
"""


def canUnlockAll(boxes):
    """
    This funciton determines if all the boxes can be unlocked
    """
    if not boxes:
        return True
    unlocked = set()
    unlocked.add(0)
    unchecked = set(range(len(boxes)))
    while len(unlocked) != len(boxes):
        checked = set()
        previous_len = len(unlocked)
        for i in unchecked:
            if i in unlocked:
                checked.add(i)
                for key in boxes[i]:
                    unlocked.add(key)
        current_len = len(unlocked)
        unchecked = unchecked.difference(checked)
        if previous_len == current_len:
            return False
    return True
