#!/usr/bin/python3
"""
Implemented using graph and a deep search algorithm
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you. Each box is
    numbered sequentially from
    0 to n - 1 and each box may contain keys to the other boxes.
    """
    opened = set()
    key_box = {}
    idx = 0
    for box in boxes:
        key_box[str(idx)] = box
        idx += 1

    stack = [0]
    while len(stack) > 0:
        current = stack.pop()
        opened.add(current)
        for key in key_box[str(current)]:
            if key in opened:
                continue
            stack.append(key)
    return len(opened) == len(boxes)