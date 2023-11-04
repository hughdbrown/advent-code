#!/usr/bin/env python
from __future__ import print_function

from collections import Counter, defaultdict
import re
from operator import itemgetter, attrgetter
import types
from itertools import chain, combinations, permutations
import os.path
from pprint import pprint
from string import lowercase
from hashlib import md5

import simplejson



class Spell(object):
    def __init__(self, player, cost):
        

class MM(Spell):
    def __init__(self):
        pass
    def play(self, player1, player2):
        player1["m"] -= 53
        player2["h"] -= 4

class Drain(Spell):
    def __init__(self):
        pass
    def play(self, player1, player2):
        player1["m"] -= 73
        player1["h"] += 2
        player2["h"] -= 2

class Shield(Spell):
    def __init__(self):
        pass
    def play(self, player1, player2):
        if self.turns == 0:
            self.armor -= 7
        elif self.turns == 6:
            self.armor += 7
        self.turns -= 1

spells = {
    "mm": 
}

def play(player1, player2):
    


def main(d):
    player1 = {"h": 50, "d": 0, "m": 500, "s": [], "a": 0}
    player2 = {"h": 71, "d": 10}
    return None


def main2(d):
    return None



if __name__ == '__main__':
    d = None
    print(main(d))
    print(main2(d))
