#!/usr/bin/env python
from __future__ import print_function

from collections import defaultdict

def primes(n):
    def mark(low, high, m):
        for j in range(low * low, high + 1, low):
            m[j] = 0
    m = [0, 0] + ([1] * (n + 1))
    mark(2, n, m)
    for i in range(3, n + 1, 2):
        if m[i]:
            mark(i, n, m)
    return [i for i in range(n + 1) if m[i]]


PRIMES = primes(10 * 1000 * 1000)

def gifts(x):
    """
    >>> gifts(1)
    set([1])
    >>> gifts(2)
    set([2, 1])
    >>> gifts(3)
    set([3, 1])
    >>> gifts(4)
    set([4, 1, 2])
    >>> gifts(5)
    set([5, 1])
    >>> gifts(6)
    set([6, 1, 2, 3])
    >>> gifts(7)
    set([7, 1])
    >>> gifts(8)
    set([8, 1, 2, 4])
    >>> gifts(9)
    set([9, 1, 3])
    """
    return set([x] + [i for i in range(1, int(x // 2) + 1) if x % i == 0])


def gifts2(x):
    return set([x] + [i for i in range(max(1, x // 50), int(x // 2) + 1) if x % i == 0])


def main(n):
    g = {}
    m = 0
    for i in range(1, n):
        for j in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79):
            k = i // j
            if (k * j == i) and k in g:
                orig = g[k]
                g[i] = orig.union(set(j * a for a in orig))
                break
        else:
            g[i] = gifts(i)
        s = sum(g[i])
        if s > m:
            m = s
            if 10 * s >= n:
                print("Found {0} {1}".format(g[i], i))
                return i


def main2(n):
    m = 0
    for i in range(180, 400 * 1000 * 1000, 180):
        if i not in PRIMES:
            s = gifts2(i)
            ss = sum(s)
            if ss > m:
                m = ss
                if ss * 11 >= n:
                    print(i, ss, sorted(s))
                    return i


if __name__ == '__main__':
    from doctest import testmod
    testmod()
    print(main(36 * 1000 * 1000))
    print(main2(36 * 1000 * 1000))
