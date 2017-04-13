#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib
import urlparse
import re


def url2domain(url):
    try:
        a = urlparse.urlparse(urllib.unquote(url.strip()))
        if a.scheme in ['http', 'https']:
            b = re.search("(?:www\.)?(.*)", a.netloc).group(1)
            if b is not None:
                return str(b).strip()
            else:
                return
        else:
            return
    except:
        return


def do_map(record):
    try:
        (uid, _, url) = record.split()
        url1 = url2domain(url)
        if uid and url1:
            if uid != '-' and url1 != '-':
                yield uid, url1
    except ValueError:
        yield


def main():
    # with open('/Users/usual/PycharmProjects/first/data/inLab02s.txt', 'r') as ff:
    for line in sys.stdin:
        # for line in ff:
        ll = [x for x in do_map(line) if x]
        if ll:
            (url, val) = ll[0]
            print '%s\t%s' % (url, val)


if __name__ == "__main__":
    main()
