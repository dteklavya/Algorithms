#!/usr/bin/env python

import sys


def get_sum(a, b):
    if a == b:
        return a
    l = max(a, b)
    s = min(a, b)
    sum = 0
    s = s - 1
    for i in range(l, s, -1):
        sum = sum + i
    return sum

##print get_sum(int(sys.argv[1]), int(sys.argv[2]))

import re


def validate_pin(pin):
    length = len(pin)
    if length != 4 and length != 6:
        return False
    regex = re.compile("[^0-9]")
    if re.search(regex, pin):
        return False
    return True


print validate_pin(sys.argv[1])
