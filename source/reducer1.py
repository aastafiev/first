#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_reduce(key, values):
        yield key, sum(values)


def main():
    prev_key = None
    values = []

    for line in sys.stdin:
        key, v = line.split()
        if key != prev_key and prev_key is not None:
            for (result_key, sum_v) in do_reduce(prev_key, values):
                print '%s\t%d' % (result_key, sum_v)
            values = []
        prev_key = key
        values.append(int(v))

    if prev_key is not None:
        for (result_key, sum_v) in do_reduce(prev_key, values):
            print "%s\t%d" % (result_key, sum_v)


if __name__ == "__main__":
    main()
