#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """ 
    fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    the_change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        the_change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return the_change
