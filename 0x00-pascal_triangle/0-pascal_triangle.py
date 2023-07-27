#!/usr/bin/python3
"""
Created by Jenaide Sibolie

0 - Pascal's Triangle
"""


def pascal_triangle(n):
    """A function pascal_triangle that returns a list of integers
    representing the Pascal triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        previous_row = triangle[i - 1]

        for x in range(1, i):
            row.append(previous_row[x - 1] + previous_row[x])

        row.append(1)
        triangle.append(row)

    return triangle
