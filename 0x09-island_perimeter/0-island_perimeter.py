#!/usr/bin/python3
"""Conatians a function that return perimeter of island"""


def island_perimeter(grid):
    """Return the perimeter of an island."""

    rows = len(grid)
    columns = len(grid[0])

    perimeter = 0
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                perimeter += 4

                if column > 0 and grid[row][column - 1] == 1:
                    perimeter -= 2

                if row > 0 and grid[row - 1][column] == 1:
                    perimeter -= 2

    return perimeter
