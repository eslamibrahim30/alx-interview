#!/usr/bin/python3
"""
This module for task "Log parsing"
"""
import sys
import re
import signal
total_size = 0
counter = 0
status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
date_pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]"
source = r'"GET /projects/260 HTTP/1.1"'
number = r"\d{1,4}"
regex_rep = "{} - {} {} {} {}".format(
    ip_pattern, date_pattern, source, number, number
)
pattern = re.compile(regex_rep)


def print_info():
    print("File size: {}".format(total_size))
    for key in status_code:
        if status_code[key] != 0:
            print("{}: {}".format(key, status_code[key]))
    return None


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            line = line.rstrip()
            if re.match(pattern, line) is not None:
                total_size += int(line.split()[-1])
                status_code[line.split()[-2]] += 1
                counter += 1
            if counter == 10:
                print_info()
                counter = 0
    except KeyboardInterrupt:
        print_info()
