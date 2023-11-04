#!/usr/bin/env python
from __future__ import print_function

import numpy as np

SIZE = 100

def load_data():
    with open("data/advent-18.txt") as f:
        return [line.rstrip() for line in f]

def possible(i, j):
    x = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]
    return [(m, n) for m, n in x if 0 <= m < SIZE and 0 <= n < SIZE]

N = {
    (i, j): possible(i, j)
    for i in range(SIZE)
    for j in range(SIZE)
}

CORNERS = set([(0, 0), (0, SIZE - 1), (SIZE - 1, 0), (SIZE - 1, SIZE - 1)])

def neighbors(d, i, j):
    x = N[(i, j)]
    return np.sum(d[m, n] for m, n in x)


def transform(d):
    """
    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    """
    new_board = np.zeros((SIZE, SIZE), dtype=np.int)
    for i in range(SIZE):
        row = d[i]
        for j in range(SIZE):
            n = neighbors(d, i, j)
            v = n in (2, 3) if row[j] else n == 3
            new_board[i, j] = int(v)
    return new_board


def main(d):
    for _ in range(SIZE):
        d = transform(d)
    return np.sum(d)


def transform2(d):
    """
    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    """
    new_board = np.zeros((SIZE, SIZE), dtype=np.int)
    for i in range(SIZE):
        row = d[i]
        for j in range(SIZE):
            if (i, j) in CORNERS:
                v = 1
            else:
                n = neighbors(d, i, j)
                v = n in (2, 3) if row[j] else n == 3
            new_board[i, j] = int(v)
    return new_board


def main2(d):
    for _ in range(SIZE):
        d = transform2(d)
    return np.sum(d)


if __name__ == '__main__':
    d = load_data()
    data = np.zeros((SIZE, SIZE))
    for i in range(SIZE):
        for j in range(SIZE):
            data[i, j] = int(d[i][j] == '#')
    print(main(data))
    print(main2(data))
