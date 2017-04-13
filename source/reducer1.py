#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def do_reduce(key, values):
    cat1 = [u'cars.ru', u'avto-russia.ru', u'bmwclub.ru']
    cat2 = [u'fastpic.ru', u'fotoshkola.net', u'bigpicture.ru']
    cat3 = [u'nirvana.fm', u'rusradio.ru', u'pop-music.ru']
    cat4 = [u'snowmobile.ru', u'nastroisam.ru', u'mobyware.ru']
    is_cat1, is_cat2, is_cat3, is_cat4 = 0, 0, 0, 0

    for ss in cat1:
        if values.count(ss) >= 10:
            is_cat1 = 1
    for ss in cat2:
        if values.count(ss) >= 10:
            is_cat2 = 1
    for ss in cat3:
        if values.count(ss) >= 10:
            is_cat3 = 1
    for ss in cat4:
        if values.count(ss) >= 10:
            is_cat4 = 1
    yield key, is_cat1, is_cat2, is_cat3, is_cat4


def main():
    prev_key = None
    values = []

    for line in sys.stdin:
        key, v = line.split()
        if key != prev_key and prev_key is not None:
            for result_key, cat1, cat2, cat3, cat4 in do_reduce(prev_key, values):
                print '%s\t%s\t%s\t%s\t%s' % (result_key, cat1, cat2, cat3, cat4)
            values = []
        prev_key = key
        values.append(str(v))

    if prev_key is not None:
        for result_key, cat1, cat2, cat3, cat4 in do_reduce(prev_key, values):
            print "%s\t%s\t%s\t%s\t%s" % (result_key, cat1, cat2, cat3, cat4)


if __name__ == "__main__":
    main()
