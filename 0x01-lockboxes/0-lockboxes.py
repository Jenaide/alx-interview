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
    for key in range(1, len(boxes) - 1):
        num_box = False
        for index in range(len(boxes)):
            num_box = key in boxes[index] and key != index
            if num_box:
                break
        if num_box is False:
            return num_box
    return True
