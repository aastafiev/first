#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_reduce(key, value, in_dic):
    if key not in in_dic:
        in_dic[key] = float(value)
    else:
        in_dic[key] += float(value)
    # return in_dic


def main():
    out = dict()

    for line in sys.stdin:
        ip, userid, country, bannerid, payout = line.split(",")
        # out = do_reduce(country, payout, out)
        do_reduce(country.strip(), payout.strip(), out)

    for key, value in out.iteritems():
        print "%s, %.2f" % (key, value)


if __name__ == "__main__":
    main()
