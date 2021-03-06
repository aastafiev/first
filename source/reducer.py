#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_reduce(key, values):
    return key, sum(values)


def main():
    prev_key = None
    values = []

    for line in sys.stdin:
        key, value = line.split("\t")
        if key != prev_key and prev_key is not None:
            result_key, result_value = do_reduce(prev_key, values)
            print "%s, %.2f" % (result_key, result_value)
            values = []
        prev_key = key
        values.append(float(value))

    if prev_key is not None:
        result_key, result_value = do_reduce(prev_key, values)
        print "%s, %.2f" % (result_key, result_value)


if __name__ == "__main__":
    main()