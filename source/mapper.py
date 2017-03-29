#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_map(record, idx_key, idx_value, separator=''):
    columns = record.split(separator)
    yield columns[idx_key].strip(), columns[idx_value].strip()


def main():
    for line in sys.stdin:
        for key, value in do_map(line, 2, 4, ','):
            print "%s\t%s" % (key, value)


if __name__ == "__main__":
    main()
