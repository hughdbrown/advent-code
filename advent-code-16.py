#!/usr/bin/env python
from __future__ import print_function

from collections import Counter, defaultdict
import re
from operator import itemgetter, attrgetter, le, ge, eq
import types
from itertools import chain, combinations, permutations
import os.path
from pprint import pprint
from string import lowercase
from hashlib import md5

import simplejson

answer = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

def load_data():
    with open("data/advent-16.txt") as f:
        return simplejson.loads(f.read())

def main(d):
    for sk, sv in d.items():
        if all(answer[k] == v for k, v in sv.items()):
            return sk


def main2(d):
    op = {
        'cats': le,
        'trees': le,
        'pomeranians': ge,
        'goldfish': ge,
    }
    for sk, sv in d.items():
        if sum(
            int(op.get(k, eq)(answer[k], v))
            for k, v in sv.items()) == 3:
            return sk



if __name__ == '__main__':
    d = load_data()
    print(main(d))
    print(main2(d))
