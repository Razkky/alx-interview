#!/usr/bin/python3
"""Return list of integer representing the pascal triangle of n"""


def pascal_triangle(n: int) -> list:
    """Return a list of integer representing a pascal triangle of n"""

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        row.append(1)
        triangle.append(row)

    return triangle
