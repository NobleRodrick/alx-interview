#!/usr/bin/python3
"""
Solves the lock boxes puzzle
"""


def next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    the_dict = {}
    while True:
        if len(the_dict) == 0:
            the_dict[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = next_opened_box(the_dict)
        if keys:
            for key in keys:
                try:
                    if the_dict.get(key) and the_dict.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    the_dict[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in the_dict.values()]:
            continue
        elif len(the_dict) == len(boxes):
            break
        else:
            return False

    return len(the_dict) == len(boxes)


def main():
    """
    Entry point
    """
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
