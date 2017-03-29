#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_map(record):
    (uid, ts, url) = record.split()
    yield uid, ts, url


def main():
    for line in sys.stdin:
        for (uid, ts, url) in do_map(line):
            print "%s\t%s\t%s" % (uid, ts, url)


if __name__ == "__main__":
    main()
