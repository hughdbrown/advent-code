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
        if item == size:
            yield [item]
        elif item < size:
            for x in fit(d[i + 1:], size - item):
                yield [item] + x


def main(d, size):
    return len(list(fit(d, size)))


def main2(d, size):
    x = sorted(fit(d, size), key=len)
    return len(list(takewhile(lambda xx: len(xx) == len(x[0]), x)))


if __name__ == '__main__':
    d = load_data()
    print(main(d, 150))
    print(main2(d, 150))
