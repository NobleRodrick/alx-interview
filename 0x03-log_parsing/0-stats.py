#!/usr/bin/python3

import sys


def print_the_message(status_code_dict, complete_sizeof_file):
    """
    Method to print
    Args:
        status_code_dict: dict of status codes
        complete_sizeof_file: total size of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(complete_sizeof_file))
    for key, val in sorted(status_code_dict.items()):
        if val != 0:
            print("{}: {}".format(key, val))


complete_sizeof_file = 0
code = 0
counter_variable = 0
status_code_dict = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        the_parsed_line = line.split()  # trimming action
        the_parsed_line = the_parsed_line[::-1]  # inverting action

        if len(the_parsed_line) > 2:
            counter_variable += 1

            if counter_variable <= 10:
                complete_sizeof_file += int(the_parsed_line[0])  # file size
                code = the_parsed_line[1]  # status code

                if (code in status_code_dict.keys()):
                    status_code_dict[code] += 1

            if (counter_variable == 10):
                print_the_message(status_code_dict, complete_sizeof_file)
                counter_variable = 0

finally:
    print_the_message(status_code_dict, complete_sizeof_file)
