#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
import sys


def is_valid(board, row, col):
    for prev_row in range(row):
        if board[prev_row] == col or \
           board[prev_row] - prev_row == col - row or \
           board[prev_row] + prev_row == col + row:
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)

def print_solution(solution):
    for row, col in solution:
        print(f'[{row}, {col}]', end=' ')
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    for sol in solutions:
        print_solution(sol)
