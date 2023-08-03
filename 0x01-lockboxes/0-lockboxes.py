#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""


def canUnlockAll(boxes):
    """
    - Determine if all boxes can be opened

    Parameters
    - Box (list of ints): list with keys for boxes.

    Return
    - True if all boxes were opened, or False if not
    """
    x = len(boxes) # number of boxes
    visited = [False] * x # keeping track of visited boxes
    stack = [0] # starts with the first box

    while stack:
        num_box = stack.pop()
        if not visited[num_box]:
            visited[num_box] = True
            keys = boxes[num_box]
            stack.extend(keys)

    return all(visited)
