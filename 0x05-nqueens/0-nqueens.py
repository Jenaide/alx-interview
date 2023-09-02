#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
import sys


def is_valid(board, row, col):
    """
    checks if theres a queen vertically or 
    diagonally in a row
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
               return False
    return True
    

def solve_nqueens(board, row):
    if row == len(board):
        print([[i, board[i]] for i in range(len(board))])
        return
    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)


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
    board = [-1] * N
    solve_nqueens(board, 0)
