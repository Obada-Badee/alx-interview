#!/usr/bin/python3
""" Log parsing Module """
import sys
import re


def print_info(total_size, code_dict):
    """Prints the desired infos """

    print(f'File size: {total_size}', flush=True)
    for code, status in code_dict.items():
        if status > 0:
            print(f"{code}: {status}", flush=True)


def main():
    """Main entry point of the program"""

    total_size = 0
    counter = 0
    code_dict = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    try:
        for line in sys.stdin:
            info_list = line.strip().split()
            file_size = info_list[-1]
            current_code = info_list[-2]

            code_dict[current_code] += 1
            total_size += file_size
            counter += 1
            if counter % 10 == 0:
                print_info(total_size, code_dict)
    except (KeyboardInterrupt, EOFError):
        print_info(total_size, code_dict)

if __name__ == "__main__":

    main()
