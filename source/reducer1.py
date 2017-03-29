#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_reduce(key, values):
    for (ts, url) in values:
        yield key, ts, url


def main():
    prev_key = None
    values = []

    for line in sys.stdin:
        key, ts, url = line.split()
        if key != prev_key and prev_key is not None:
            for (result_key, result_ts, result_url) in do_reduce(prev_key, values):
                print "%s\t%s\t%s" % (result_key, result_ts, result_url)
            values = []
        prev_key = key
        values.append((ts, url))

    if prev_key is not None:
        for (result_key, result_ts, result_url) in do_reduce(prev_key, values):
            print "%s\t%s\t%s" % (result_key, result_ts, result_url)


if __name__ == "__main__":
    main()
