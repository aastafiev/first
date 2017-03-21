#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def main():
    for ln in sys.stdin:
        for s in ln.split(' '):
            print "%s 1" % s


if __name__ == "__main__":
    main()
