#!/usr/bin/python3
"""Alx interview question
  - Prime Game
"""


def isWinner(x, nums):
    """ function that determines the winner of a prime game
    """
    winner_counter = {'Maria': 0, 'Ben': 0}

    for n in nums:
        round_winner = isRoundWinner(n)
        if round_winner is not None:
            winner_counter[round_winner] += 1

    if winner_counter['Maria'] > winner_counter['Ben']:
        return 'Maria'
    elif winner_counter['Ben'] > winner_counter['Maria']:
        return 'Ben'
    else:
        return None

def isRoundWinner(n):
    list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        current_player = players[i % 2]
        selected_id = []
        prime = -1
        for win, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    selected_id.append(win)
            else:
                if isPrime(num):
                    selected_id.append(win)
                    prime = num
        if prime == -1:
            return players[1 if current_player == players[0] else 0]
        else:
            list = [list[win] for win in range(len(list)) if win not in selected_id]
    return None

def isPrime(n):
    if n < 2 or (n > 2 and n % 2 == 0):
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
