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