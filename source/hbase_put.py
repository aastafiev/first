#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import happybase as hbase


def main():
    conn = hbase.Connection('node2.newprolab.com')
    table = conn.table('alexey.astafiev')

    for line in sys.stdin:
        key, ts, url = line.split()
        table.put(key, {'data:url': url}, timestamp=int(ts))


if __name__ == "__main__":
    main()
