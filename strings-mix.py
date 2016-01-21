#!/usr/bin/python

import sys
from string import ascii_lowercase


def mix(s1, s2):
    d1 = dict()
    d2 = dict()
    for c in s1:
        if c not in ascii_lowercase:
            continue
        if c in d1:
            d1[c] = d1[c] + 1
        else:
            d1[c] = 1
    for c in s2:
        if c not in ascii_lowercase:
            continue
        if c in d2:
            d2[c] = d2[c] + 1
        else:
            d2[c] = 1

    res = dict()
    for c in d1:
        if d1[c] > 1:
            if c in d2 and d1[c] == d2[c]:
                res['=:' + c * d1[c]] = d1[c]
            else:
                if c not in d2 or d2[c] < d1[c]:
                    res['1:' + c * d1[c]] = d1[c]
    for c in d2:
        if d2[c] > 1:
            if c in d1 and d2[c] == d1[c]:
                continue
            else:
                if c not in d1 or d1[c] < d2[c]:
                    res['2:' + c * d2[c]] = d2[c]

    return '/'.join(sorted(res, key=lambda k: (-res[k], k)))


print mix(sys.argv[1], sys.argv[2])
