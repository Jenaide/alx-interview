#!/usr/bin/python3
"""making change module.
"""


def makeChange(coins, total):
    """determine the fewest number of coins 
    needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    jen = total
    count = 0
    gem = 0
    sort_coin = sorted(coins, reverse=True)
    x = len(coins)

    while jen > 0:
        if gem >= x:
            return -1

        if jen - sort_coin[gem] >= 0:
            jen -= sort_coin[gem]
            count += 1
        else:
            gem += 1
    return count
