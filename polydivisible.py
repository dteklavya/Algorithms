#!/usr/bin/env python

import sys


def is_polydivisible(n, b):
    n = str(n)
    b = int(b)
    length = len(n)
    for i in range(1, length + 1):
        print "Num: ", int(n[:i]), " in base 10 ", int(n[:i], base=b), " mod ", i
        if int(n[:i], base=b) % i == 0:
            continue
        else:
            return False
    return True


print is_polydivisible(sys.argv[1], sys.argv[2])
