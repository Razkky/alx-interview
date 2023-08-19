#!/usr/bin/python3
"""Calcualte minimum opereaton needed to result to n H"""

def minOperations(n):
    """Function to calcualte the minimum operations to result to n H"""

    if n <= 0:
        return 0

    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    return sum(factors)
