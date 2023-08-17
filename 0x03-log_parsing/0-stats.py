#!/usr/bin/python3
"""
Created by Jenaide Sibolie.
A script to parse HTTP requests logs.
"""
import sys


def print_msg(dict_sc, total_file_size):
    """
    Print method
    Args:
        status_codes: dict of status codes
        total_file_size: total of the file
    Return: Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


total_file_size = 0
code = 0
counter = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in status_codes.keys()):
                    status_codes[code] += 1

            if (counter == 10):
                print_msg(status_codes, total_file_size)
                counter = 0

finally:
    print_msg(status_codes, total_file_size)
