#!/usr/bin/env python
from __future__ import print_function

from collections import Counter, defaultdict
import re
from operator import itemgetter


def load_data():
    regex = re.compile(r"""(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<time>\d+) seconds, but then must rest for (?P<rest>\d+) seconds.""")
    with open("data/advent-14.txt") as f:
        data = []
        for line in f:
            g = regex.match(line).groupdict()
            data.append({k: t(g[k]) for k, t in zip(("name", "speed", "time", "rest"), (str, int, int, int))})
    return data


def distance(r, time):
    t = r["time"]
    m, n = divmod(time, (t + r["rest"]))
    max_flying = (t * m) + min(n, t)
    return r["speed"] * max_flying


def main(d, time):
    return max(distance(r, time) for r in d)


def main2(d, time):
    score = Counter()
    for i in range(1, time + 1):
        steps = {r["name"]: distance(r, i) for r in d}
        max_distance = max(steps.items(), key=itemgetter(1))[1]
        for name, dist in steps.items():
            if dist == max_distance:
                score[name] += 1
    return max(score.values())


if __name__ == '__main__':
    d = load_data()
    print(main(d, 2503))
    print(main2(d, 2503))
