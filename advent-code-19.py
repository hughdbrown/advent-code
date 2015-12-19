#!/usr/bin/env python
from __future__ import print_function

from collections import defaultdict
from pprint import pprint


def chemsplit(ed, v):
    result = []
    i = 0
    # Make a lookup table based on matches on first letter
    lookup = defaultdict(list)
    for k in ed:
        lookup[k[0]].append(k)
    while i < len(v):
        c = v[i]
        for k in sorted(lookup[c], key=len, reverse=True):
            if v[i:].startswith(k):
                i += len(k)
                result.append(ed[k])
                break
    return result

def load_data():
    d = defaultdict(list)
    subs = [
        ("Al", "ThF"),
        ("Al", "ThRnFAr"),
        ("B", "BCa"),
        ("B", "TiB"),
        ("B", "TiRnFAr"),
        ("Ca", "CaCa"),
        ("Ca", "PB"),
        ("Ca", "PRnFAr"),
        ("Ca", "SiRnFYFAr"),
        ("Ca", "SiRnMgAr"),
        ("Ca", "SiTh"),
        ("F", "CaF"),
        ("F", "PMg"),
        ("F", "SiAl"),
        ("H", "CRnAlAr"),
        ("H", "CRnFYFYFAr"),
        ("H", "CRnFYMgAr"),
        ("H", "CRnMgYFAr"),
        ("H", "HCa"),
        ("H", "NRnFYFAr"),
        ("H", "NRnMgAr"),
        ("H", "NTh"),
        ("H", "OB"),
        ("H", "ORnFAr"),
        ("Mg", "BF"),
        ("Mg", "TiMg"),
        ("N", "CRnFAr"),
        ("N", "HSi"),
        ("O", "CRnFYFAr"),
        ("O", "CRnMgAr"),
        ("O", "HP"),
        ("O", "NRnFAr"),
        ("O", "OTi"),
        ("P", "CaP"),
        ("P", "PTi"),
        ("P", "SiRnFAr"),
        ("Si", "CaSi"),
        ("Th", "ThCa"),
        ("Ti", "BP"),
        ("Ti", "TiTi"),
        ("e", "HF"),
        ("e", "NAl"),
        ("e", "OMg"),
    ]
    elems = ["Al", "B", "C", "Ca", "F", "H", "Mg", "N", "O", "P", "Si", "Th", "Ti", "Rn", "Ar", "Y", "e"]
    ed = {k: i for i, k in enumerate(elems)}
    for k, v in subs:
        kk = ed[k]
        vv = chemsplit(ed, v)
        # print(kk, vv)
        d[kk].append(vv)
    equation = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
    return d, chemsplit(ed, equation), elems


def search(src, target):
    results = []
    src = list(src)
    target = list(target)
    s = len(src)
    t = len(target)
    for i in range(0, s - t + 1):
        if src[i:i + t] == target:
            results.append(i)
    return results


def main(d, equation):
    s = set()
    for k, v in d.items():
        # Find all the indexes that k matches equation at
        for index in search(equation, [k]):
            # Do all possible substitutions at matching indexes
            assert equation[index] == k
            left, right = equation[:index], equation[index + 1:]
            s.update([tuple(left + vv + right) for vv in v])
    return len(s)


def main2(src, d, target):
    reverse_dict = {
        tuple(vv): k
        for k, v in d.items()
        for vv in v
    }
    # pprint(reverse_dict)
    subs = 0
    while target != src:
        print('-' * 30)
        possible = set(target)
        keyorder = sorted([k for k in reverse_dict if set(k).issubset(possible)], key=len, reverse=True)
        for k in keyorder:
            v = reverse_dict[k]
            print("{1}: Trying key {0}".format(k, target))
            for index in list(reversed(search(target, k))):
                left, right = target[:index], target[index + len(k):]
                target = left + [v] + right
                subs += 1
                print("{0} -> {1}".format(k, target))
    return subs


if __name__ == '__main__':
    d, equation, elems = load_data()
    print(main(d, equation))
    print(main2([elems.index("e")], d, equation))
