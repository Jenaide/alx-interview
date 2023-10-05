#!/usr/bin/python3
"""Alx interview question
  - Prime Game
"""


def isWinner(x, nums):
    """ function that determines the winner of a prime game
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def canWin(n):
        # Create a memoization table to store the results for different n values
        memo = {}

        # Base case: If n is 1, the current player loses
        if n == 1:
            return False

        # Check if the result is already computed
        if n in memo:
            return memo[n]

        # Try all prime numbers less than or equal to n
        for i in range(2, n + 1):
            if is_prime(i):
                # If the current player can make a move that leads to a losing state for the opponent,
                # they win the game
                if not canWin(n - i):
                    memo[n] = True
                    return True

        # If the current player cannot make any move that leads to a losing state for the opponent,
        # they lose the game
        memo[n] = False
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
