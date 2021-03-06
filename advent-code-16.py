#!/usr/bin/env python
from __future__ import print_function

from operator import le, ge, eq

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


def main(d, op):
    for sk, sv in d.items():
        if all(
            op.get(k, eq)(answer[k], v)
            for k, v in sv.items()):
            return sk


if __name__ == '__main__':
    d = load_data()
    print(main(d, {}))
    op = {
        'cats': le,
        'trees': le,
        'pomeranians': ge,
        'goldfish': ge,
    }
    print(main(d, op))
