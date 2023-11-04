#!/usr/bin/env python
from __future__ import print_function

from collections import Counter, defaultdict, OrderedDict
import re
from operator import itemgetter, attrgetter, __mul__
import types
from itertools import chain, combinations, permutations
import os.path
from pprint import pprint
from string import lowercase
from hashlib import md5

import simplejson

KEYS2 = ("capacity", "durability", "flavor", "texture", "calories")


def load_data():
    regex = re.compile(r"""
        (?P<name>\w+):\s
        capacity\s(?P<capacity>-?\d),\s
        durability\s(?P<durability>-?\d),\s
        flavor\s(?P<flavor>-?\d),\s
        texture\s(?P<texture>-?\d),\s
        calories\s
        (?P<calories>-?\d)
    """, re.VERBOSE)
    with open("data/advent-15.txt") as f:
        giter = [regex.match(line.rstrip()).groupdict() for line in f]
        pairs = (("name", str), ("capacity", int), ("durability", int), ("flavor", int), ("texture", int), ("calories", int))
        return [
            OrderedDict((k, t(g[k])) for k, t in pairs)
            for g in giter
        ]


def score(t):
    return reduce(lambda x, tt: x * max(tt, 0), t, 1)


def outcome(d, i, j, k, l):
    return OrderedDict(
        (key, sum(x * dd[key] for x, dd in zip((i, j, k, l), d)))
        for key in KEYS2
    )


def counter_iter():
    for i in range(100 + 1 - 3):
        for j in range(100 + 1 - i - 2):
            for k in range(100 + 1 - i - j - 1):
                l = 100 - i - j - k
                yield (i, j, k, l)


def main(d):
    s = 0
    for i, j, k, l in counter_iter():
        o = outcome(d, i, j, k, l)
        c = o.pop("calories")
        s = max(score(o.values()), s)
    return s


def main2(d):
    """
    Restrict solutions to those with 500 calories
    """
    s = 0
    for i, j, k, l in counter_iter():
        o = outcome(d, i, j, k, l)
        c = o.pop("calories")
        if c == 500:
            s = max(score(o.values()), s)
    return s


if __name__ == '__main__':
    d = load_data()
    print(main(d))
    print(main2(d))
