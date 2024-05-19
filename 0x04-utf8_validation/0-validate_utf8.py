#!/usr/bin/python3
"""
This module for task "UTF-8 Validation"
"""


def countFirstOnes(byte):
    """
    This method counts the first consecutive ones in a byte.
    """
    ones = 0
    cmp = 1 << 7
    while byte & cmp:
        ones += 1
        cmp = cmp >> 1
    return ones


def validUTF8(data):
    """
    This method determines if a given data set represents
    a valid UTF-8 encoding.
    """
    idx = 0
    while idx < len(data):
        n_bytes = countFirstOnes(data[idx])
        if idx + n_bytes - 1 >= len(data):
            return False
        elif data[idx] > 255:
            return False
        elif n_bytes == 0:
            idx += 1
        else:
            idx += 1
            n_bytes -= 1
            while n_bytes:
                if (data[idx] >> 6) ^ 2:
                    return False
                if data[idx] > 255:
                    return False
                idx += 1
                n_bytes -= 1
    return True
