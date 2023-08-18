#!/usr/bin/python3
"""This scripts has a function that determines if all boxes can be unlocked """


def canUnlockAll(boxes):
    """Check if boxes can be unlocked"""

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    for box_status in unlocked:
        if not box_status:
            return False
    return True
