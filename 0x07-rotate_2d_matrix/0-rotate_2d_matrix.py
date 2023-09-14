#!/usr/bin/python3
"""
Rotate 2D Matrix
"""
def rotate_2d_matrix(matrix):
    """2D matrix that rotates an n by n
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap elements across the main diagonal)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
