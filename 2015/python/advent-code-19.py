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
    lookup = {k: sorted(v, key=len, reverse=True) for k, v in lookup.items()}
    while i < len(v):
        for k in lookup[v[i]]:
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
    src, target = list(src), list(target)
    t = len(target)
    t0 = target[0]
    possible = [i for i, s0 in enumerate(src) if s0 == t0]
    return [i
        for i in reversed(possible)
        if src[i:i + t] == target
    ]


def main(d, equation):
    segment_iter = (
        (equation[:index], equation[index + 1:], v)
        for k, v in d.items()
        for index in search(equation, [k])
    )
    return len(set(
        tuple(left + vv + right)
        for left, right, v in segment_iter
        for vv in v
    ))


def main2(src, d, target):
    reverse_dict = {
        tuple(vv): [k]
        for k, v in d.items()
        for vv in v
    }
    sorted_keys = sorted(reverse_dict, key=len, reverse=True)
    # pprint(reverse_dict)
    subs = 0
    while target != src:
        # print('-' * 30)
        possible = set(target)
        keyorder = (k for k in sorted_keys if set(k).issubset(possible))
        for k in keyorder:
            klen = len(k)
            vlist = reverse_dict[k]
            # print("{1}: Trying key {0}".format(k, target))
            index_matches = list(search(target, k))
            for index in index_matches:
                left, right = target[:index], target[index + klen:]
                target = left + vlist + right
                # print("{0} -> {1}".format(k, target))
            subs += len(index_matches)
    return subs


if __name__ == '__main__':
    d, equation, elems = load_data()
    print(main(d, equation))
    print(main2([elems.index("e")], d, equation))
