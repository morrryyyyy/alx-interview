#!/usr/bin/python3
"""This is the 0-pascal's triangle module."""


def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return []
    i = 0
    for i in range(n):
        row = []
        j = 0
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                element = triangle[i - 1][j] + triangle[i - 1][j - 1]
                row.append(element)
        triangle.append(row)
    return triangle
