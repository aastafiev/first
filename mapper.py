#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_map(record):
    for word in record.split():
        yield word.lower(), 1


def main():
    for line in sys.stdin:
        for key, value in do_map(line):
            print(key + "\t" + str(value))


if __name__ == "__main__":
    main()
