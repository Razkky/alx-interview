#!/usr/bin/env python3
"""This script checks if a data is utf-8 encoding"""


def validUTF8(data):
    """Check if a data is a valid utf8 data"""

    def check(num):
        mask = 1 << 7
        i:int = 0
        while num & mask:
            mask >>= 1
            i += 1
        return i

    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k > len(data):
            return False
        while i < len(data) and i <= k:
            cur = check(data[i])
            if cur != 1:
                return False
            i += 1
    return True

