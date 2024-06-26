#!/usr/bin/python3
"""
Demonstrating UTF-8 Validation
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    byte_number = 0

    first_mask = 1 << 7
    second_mask = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if byte_number == 0:

            while mask_byte & i:
                byte_number += 1
                mask_byte = mask_byte >> 1

            if byte_number == 0:
                continue

            if byte_number == 1 or byte_number > 4:
                return False

        else:
            if not (i & first_mask and not (i & second_mask)):
                    return False

        byte_number -= 1

    if byte_number == 0:
        return True

    return False
