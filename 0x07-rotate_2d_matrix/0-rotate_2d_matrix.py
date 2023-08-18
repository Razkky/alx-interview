#!/usr/bin/python3
""" A 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix) -> None:
    """Rotate a 2D matrix 90 degrees"""
    length = len(matrix)

    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(length):
        matrix[i] = matrix[i][::-1]
