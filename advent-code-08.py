#!/usr/bin/env python

from __future__ import print_function

from collections import defaultdict, Counter
import re
import os.path



def slen(s):
    s = s[1:-1]
    result = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            if s[i + 1] == 'x':
                result.append('a')
                i += 4
            elif s[i + 1] in ("'", '"', '\\'):
                result.append(s[i + 1])
                i += 2
            else:
                print(s[i + 1])
                assert False
        else:
            result.append(c)
            i += 1
    return len(result)

def tlen(s):
    #print(s)
    result = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            result.append('\\')
            result.append('\\')
            if s[i + 1] == 'x':
                result += ['x', s[i + 2], s[i + 3]]
                i += 4
            elif s[i + 1] in ("'", '"', '\\'):
                result += ['\\', s[i + 1]]
                i += 2
            else:
                # print(s[i + 1])
                assert False
        elif c in ('"', "'"):
            result += ["\\", c]
            i += 1
        else:
            result.append(c)
            i += 1
    # print(result)
    return len(result) + 2


def main1():
    filename = "data/advent-data-08.txt"
    filelen = os.path.getsize(filename)
    with open(filename, "rb") as f:
        memory = [line for line in f]
    return sum(len(x) for x in memory) - sum(slen(x) for x in memory)

def main2():
    filename = "data/advent-data-08.txt"
    filelen = os.path.getsize(filename)
    with open(filename, "rb") as f:
        memory = [line for line in f]
    return sum(tlen(x) for x in memory) - sum(len(x) for x in memory)

if __name__ == '__main__':
    # print(tlen('""'))
    # print(tlen(r'"\x27"'))
    print(main1())
    print(main2())
