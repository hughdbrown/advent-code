
from itertools import permutations


def score(series, default):
    stops = [(k1, k2) for k1, k2 in zip(series, series[1:])]
    if not all(k in d for k in stops):
        return default
    return sum(d[k] for k in stops)

def calc_shortest(d, places):
    worst = sum(d.values())
    shortest = worst
    for k in permutations(places, len(places)):
        s = score(k, worst)
        shortest = min(shortest, s)
    return shortest

def calc_longest(d, places):
    longest = 0
    for k in permutations(places, len(places)):
        s = score(k, 0)
        longest = max(longest, s)
    return longest

if __name__ == '__main__':
    d = {
        ('AlphaCentauri', 'Snowdin'): 66,
        ('AlphaCentauri', 'Tambi'): 28,
        ('AlphaCentauri', 'Faerun'): 60,
        ('AlphaCentauri', 'Norrath'): 34,
        ('AlphaCentauri', 'Straylight'): 34,
        ('AlphaCentauri', 'Tristram'): 3,
        ('AlphaCentauri', 'Arbre'): 108,
        ('Snowdin', 'Tambi'): 22,
        ('Snowdin', 'Faerun'): 12,
        ('Snowdin', 'Norrath'): 91,
        ('Snowdin', 'Straylight'): 121,
        ('Snowdin', 'Tristram'): 111,
        ('Snowdin', 'Arbre'): 71,
        ('Tambi', 'Faerun'): 39,
        ('Tambi', 'Norrath'): 113,
        ('Tambi', 'Straylight'): 130,
        ('Tambi', 'Tristram'): 35,
        ('Tambi', 'Arbre'): 40,
        ('Faerun', 'Norrath'): 63,
        ('Faerun', 'Straylight'): 21,
        ('Faerun', 'Tristram'): 57,
        ('Faerun', 'Arbre'): 83,
        ('Norrath', 'Straylight'): 9,
        ('Norrath', 'Tristram'): 50,
        ('Norrath', 'Arbre'): 60,
        ('Straylight', 'Tristram'): 27,
        ('Straylight', 'Arbre'): 81,
        ('Tristram', 'Arbre'): 90,
    }

    for (k1, k2), v in d.items():
        d[(k2, k1)] = v

    places = set([k1 for k1, _ in d.keys()])

    print(calc_shortest(d, places))
    print(calc_longest(d, places))

