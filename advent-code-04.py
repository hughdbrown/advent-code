#!/usr/bin/env python
from __future__ import print_function

from hashlib import md5


KEY = "yzbqklnj"

def main1():
    # 282749
    for i in range(1000 * 1000):
        if md5("{0}{1}".format(KEY, i)).hexdigest().startswith("00000"):
            return i

def main2():
    # 9962624
    for i in range(1000 * 1000 * 100):
        if md5("{0}{1}".format(KEY, i)).hexdigest().startswith("000000"):
            return i


if __name__ == '__main__':
    print(main1())
    print(main2())
