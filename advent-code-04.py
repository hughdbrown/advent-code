#!/usr/bin/env python
from __future__ import print_function

from hashlib import md5


KEY = "yzbqklnj"

def search(r, prefix):
    for i in r:
        if md5("{0}{1}".format(KEY, i)).hexdigest().startswith(prefix):
            return i


def main1():
    # 282749
    return search(range(1000 * 1000), "00000")


def main2():
    # 9962624
    return search(range(1000 * 1000 * 100), "000000")


if __name__ == '__main__':
    print(main1())
    print(main2())
