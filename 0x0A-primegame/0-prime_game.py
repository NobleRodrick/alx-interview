#!/usr/bin/python3
"""
    0. Prime Game - second_player and first_player are playing a game
"""


def isWinner(x, nums):
    """
    x - represents the number of rounds
    nums - The list of numbers
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    first_player = 0
    second_player = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_prime_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            first_player += 1
        else:
            second_player += 1
    if first_player > second_player:
        return "first_player"
    if second_player > first_player:
        return "second_player"
    return None


def rm_prime_multiples(ls, x):
    """
    removes multiple
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
