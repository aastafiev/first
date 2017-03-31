#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_map(record):
    (url, v) = record.split()
    yield (url, v)


def main():
    with open('/Users/usual/PycharmProjects/first/data/outLab02s.txt', 'r') as ff:
        # for line in sys.stdin:
        for line in ff:
            for (url, v) in do_map(line):
                print "%s\t%s" % (v, url)


if __name__ == "__main__":
    main()
