#!/usr/bin/python3
"""
Module for solving prime game question
"""

def isWinner(x, nums):
    """
    function that checks for the winner
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    game_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not game_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            game_filter[j] = False
    game_filter[0] = game_filter[1] = False
    y = 0
    for i in range(len(game_filter)):
        if game_filter[i]:
            y += 1
        game_filter[i] = y
    first_player = 0
    for x in nums:
        first_player += game_filter[x] % 2 == 1
    if first_player * 2 == len(nums):
        return None
    if first_player * 2 > len(nums):
        return "Maria"
    return "Ben"
