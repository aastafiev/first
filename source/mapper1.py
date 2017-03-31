#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_map(record):
    try:
        (uid, _, url) = record.split()
        if uid and url:
            if uid != '-' and url != '-':
                yield (url, 1)
    except ValueError:
        yield


def main():
    # with open('/Users/usual/PycharmProjects/first/data/inLab02s.txt', 'r') as ff:
    for line in sys.stdin:
        # for line in ff:
        ll = [x for x in do_map(line) if x]
        if ll:
            (url, val) = ll[0]
            print '%s\t%s' % (url, val)


if __name__ == "__main__":
    main()
