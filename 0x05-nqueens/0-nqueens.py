#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
import sys

def queens(N):
    def is_valid(board, row, col):
        """
        checks if theres a queen vertically in a row
        """
        for i in range(row):
            if board[i] == col:
                return False
        """
        checks if theres a queen diagonally in a row
        """
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False
        return True
    

    def solve_nqueens(board, row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1)
    """
    Creates en empty board
    """
    board = [-1] * N

    solutions = []

    """ instruction to start solving from the first row """
    solve_nqueens(board, 0)

    for sol in solutions:
        print(sol)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """ checking the value of N """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """ N-queen solved """
    queens(N)
