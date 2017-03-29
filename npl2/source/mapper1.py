#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_map(record, uidfilter):
    try:
        (uid, timestap, url) = record.split()
        if uid and timestap and url:
            if uid != '-' and url != '-':
                if int(uid) % 256 == uidfilter:
                    yield (uid, int(float(timestap) * 1000), url)
    except ValueError:
        yield


def main():
    # with open('/Users/usual/PycharmProjects/first/npl2//data/part-0000', 'r') as ff:
    uidfilter = 164 #164 #253
    for line in sys.stdin:
        # for line in ff:
        ll = [x for x in do_map(line, uidfilter=uidfilter) if x]
        if ll:
            (uid, timestamp, url) = ll[0]
            print "%s\t%s\t%s" % (uid, timestamp, url)


if __name__ == "__main__":
    main()
