#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    n_line = 0
    stop = 3

    # with open('/Users/usual/PycharmProjects/first/data/outLab02s.txt', 'r') as ff:
    for line in sys.stdin:
        # for line in ff:
        if n_line != stop:
            key, v = line.split()
            print '%s\t%s' % (key, v)
        else:
            break
        n_line += 1


if __name__ == "__main__":
    main()
