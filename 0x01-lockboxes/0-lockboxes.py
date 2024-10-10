#!/usr/bin/python3
"""
This module contains the canUnlockAll function, which checks
if all boxes can be unlocked using a depth-first search approach.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of list of int): A list where each element is a list
        containing keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    # Track which boxes have been opened
    opened = set([0])
    stack = [0]  # Start with the first box (box 0)

    # Depth-First Search (DFS) using a stack
    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in opened and 0 <= key < len(boxes):
                opened.add(key)
                stack.append(key)

# If the number of opened boxes is equal to the
# total number of boxes, return True
    return len(opened) == len(boxes)
