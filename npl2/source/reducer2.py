#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import happybase as hbase


def do_reduce(key, values):
    conn = hbase.Connection('node2.newprolab.com')
    table = conn.table('alexey.astafiev')
    for (ts, url) in values:
        table.put(key, {'data:url': url}, timestamp=int(ts))


def main():
    prev_key = None
    values = []

    for line in sys.stdin:
        key, ts, url = line.split()
        if key != prev_key and prev_key is not None:
            do_reduce(prev_key, values)
            values = []
        prev_key = key
        values.append((ts, url))

    if prev_key is not None:
        do_reduce(prev_key, values)


if __name__ == "__main__":
    main()
