#!/usr/bin/python3
"""
N Queens placement on nxn chessboard
"""


import sys


def the_solution(row, column):
    solution = [[]]
    for queen in range(row):
        solution = place_the_queen(queen, column, solution)
    return solution


def place_the_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if it_is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def it_is_safe(q, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def main_function():

    n = init()
    # generate all solutions
    solutions = the_solution(n, n)
    # print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    main_function()
