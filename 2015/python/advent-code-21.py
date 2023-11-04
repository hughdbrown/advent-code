#!/usr/bin/env python
from __future__ import print_function

from itertools import permutations
from pprint import pprint

Weapons = [
    ["Dagger",        8,     4,       0],
    ["Shortsword",   10,     5,       0],
    ["Warhammer",    25,     6,       0],
    ["Longsword",    40,     7,       0],
    ["Greataxe",     74,     8,       0],
]

Armor = [
    ["Leather",      13,     0,       1],
    ["Chainmail",    31,     0,       2],
    ["Splintmail",   53,     0,       3],
    ["Bandedmail",   75,     0,       4],
    ["Platemail",   102,     0,       5],
]

Rings = [
    ["Damage +1",    25,     1,       0],
    ["Damage +2",    50,     2,       0],
    ["Damage +3",   100,     3,       0],
    ["Defense +1",   20,     0,       1],
    ["Defense +2",   40,     0,       2],
    ["Defense +3",   80,     0,       3],
]

def play(player1, player2):
    h1, d1, a1 = player1
    h2, d2, a2 = player2
    while True:
        h2 -= max(d1 - a2, 1)
        if h2 <= 0:
            return 1
        h1 -= max(d2 - a1, 1)
        if h1 <= 0:
            return 0


def take(x, t):
    for n in t:
        for xx in permutations(x, n):
            yield xx


def trials():
    player2 = (100, 8, 2) 
    for w in take(Weapons, (1, )):
        for a in take(Armor, (0, 1)):
            for r in take(Rings, (0, 1, 2)):
                cost = (0 if not w else w[0][1]) + (0 if not a else a[0][1]) + sum(rr[1] for rr in r or [])
                damage = (0 if not w else w[0][2]) + sum(rr[2] for rr in r or [])
                armor = (0 if not a else a[0][3]) + sum(rr[3] for rr in r or [])
                player1 = (100, damage, armor)
                p = play(player1, player2)
                yield (p, cost)


def main(outcomes):
    return min(c for p, c in outcomes if p)


def main2(outcomes):
    return max(c for p, c in outcomes if not p)


if __name__ == '__main__':
    outcomes = list(trials())
    print(main(outcomes))
    print(main2(outcomes))
