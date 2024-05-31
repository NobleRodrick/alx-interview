#!/usr/bin/python3
"""
This script determines pascals triangle for any number
"""


def pascal_triangle(n):
    """
    Will return a visual representation of pascal's triangle
    """
    triangle_list = []

    # return (triangle if n <= 0)
    if n <= 0:
        return triangle_list
    for i in range(n):
        temporal_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temporal_list.append(1)
            else:
                temporal_list.append(triangle_list[i-1][j-1] + triangle_list[i-1][j])
        triangle_list.append(temporal_list)
    # print(triangle)
    return triangle_list
