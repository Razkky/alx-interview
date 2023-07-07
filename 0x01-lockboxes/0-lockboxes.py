#!/usr/bin/env python3
"""This scripts has a function that determines if all boxes can be unlocked """


def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # List to track the unlocked status of each box
    unlocked[0] = True  # The first box is initially unlocked

    # Stack to store the boxes to be explored
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Iterate over the keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True  # Unlock the box
                stack.append(key)  # Add the box to the stack for exploration

    # Check if all boxes are unlocked
    for box_status in unlocked:
        if not box_status:
            return False
    return True
