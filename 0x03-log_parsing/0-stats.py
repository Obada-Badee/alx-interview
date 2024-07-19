#!/usr/bin/python3
""" Log parsing Module """
import re


def validate_line(line):
    """
    Validates if a log line matches the specified format.
    """
    pattern = (
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] '
        r'"GET \/projects\/260 HTTP\/1\.1" \d{3} \d+$'
    )
    return re.match(pattern, line) is not None


def print_info(total_size, code_dict):
    """
    Prints the desired infos
    """

    print(f'File size: {total_size}')
    for code, status in code_dict.items():
        if status > 0:
            print(f"{code}: {status}",)


def main():
    """Main entry point of the program"""

    total_size, counter = 0, 0
    code_dict = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                 "404": 0, "405": 0, "500": 0}
    try:

        while True:
            line = input()
            info_list = line.strip().split()
            line_size = info_list[-1]
            current_code = info_list[-2]
            code_dict[current_code] += 1
            total_size += int(line_size)
            counter += 1
            if counter % 10 == 0:
                print_info(total_size, code_dict)
    except (KeyboardInterrupt, EOFError):
        print_info(total_size, code_dict)


if __name__ == "__main__":
    main()
