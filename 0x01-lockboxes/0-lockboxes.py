def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    # List to track which boxes have been opened; initialize with False
    opened = [False] * n
    opened[0] = True  # The first box is initially unlocked
    queue = [0]  # Start with the first box (index 0)

    # Process the queue while there are boxes in it
    while queue:
        present_box = queue.pop(0)  # Get the first box from the queue

        # Iterate through all keys in the current box
        for key in boxes[present_box]:
            # Check if the key is valid (within the range of boxes) and the box isn't opened yet
            if key < n and not opened[key]:
                opened[key] = True  # Mark the box as opened
                queue.append(key)  # Add the box to the queue to process its keys

    # Return True if all boxes are opened, otherwise False
    return all(opened)

# Test cases
# Test case 1: Sequential keys to open each subsequent box
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True, as all boxes can be opened sequentially

# Test case 2: More complex key distribution, but all boxes can be opened
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True, as keys are distributed to open all boxes

# Test case 3: Not all boxes can be opened (boxes[5] and boxes[6] remain closed)
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False, as there are boxes that cannot be reached
