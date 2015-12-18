#!/usr/bin/env python
from __future__ import print_function


from itertools import takewhile


def load_data():
    return sorted([
        11,
        30,
        47,
        31,
        32,
        36,
        3,
        1,
        5,
        3,
        32,
        36,
        15,
        11,
        46,
        26,
        28,
        1,
        19,
        3
    ], reverse=True)


def fit(d, size):
    for i, item in enumerate(d):
        ilist = [item]
        if item == size:
            yield ilist
        elif item < size:
            for x in fit(d[i + 1:], size - item):
                yield ilist + x


def main(fits):
    return len(fits)


def main2(fits):
    x = sorted(fits, key=len)
    return len(list(takewhile(lambda xx: len(xx) == len(x[0]), x)))


if __name__ == '__main__':
    d = load_data()
    fits = list(fit(d, 150))
    print(main(fits))
    print(main2(fits))
