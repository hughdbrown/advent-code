#!/usr/bin/env python
from __future__ import print_function

from collections import Counter, defaultdict
from string import lowercase
from hashlib import md5
import re
import os.path
from itertools import permutations, combinations
import types
from pprint import pprint

import simplejson

import numpy as np

def process(line):
    words = line.split()
    return (
        words[0],
        words[-1].replace('.', ''),
        (1 if 'gain' in words else -1) * int(re.match(r'''.*?(?P<num>\d+)''', line).groupdict()['num'])
    )

def load_data():
    with open("data/advent-13.txt") as f:
        data = [process(line.rstrip()) for line in f]
        d = defaultdict(dict)
        for k, v, n in data:
            d[k].update({v: n})
        # for k, v in d.items():
        #     print(k, v)
    return d


def pos_score(d, pos, c):
    place = {name: i for i, name in enumerate(c)}
    return sum(
        n
        for p, k in zip(pos, c)
        for v, n in d[k].items()
        if place[v] in p
    )


def precalc_pos(names):
    count = len(names)
    return [((i + count - 1) % count, (i + 1) % count) for i in range(count)]


def main(d):
    names = set(d)
    pos = precalc_pos(names)
    return max(pos_score(d, pos, c) for c in permutations(names, len(names)))


if __name__ == '__main__':
    d = load_data()
    print(main(d))
    dd = d.copy()
    for name in dd.keys():
        dd[name]['Hugh'] = 0
        dd['Hugh'][name] = 0
    print(main(dd))
