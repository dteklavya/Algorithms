#!/usr/bin/env python



import sys
import math


def ndigits(n):
    digits = 0
    if n > 0:
        digits = int(math.log10(n))+1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n))+2
    return digits


def isPalindrome(number):
    hv = ndigits(number) / 2
    div = 10 ** hv
    (q, r) = [str(i) for i in divmod(number, div)]
    print q, r
    if r[::-1] == q[0:len(r)]:
        return True
    else:
        return False

number = sys.argv[1]
print isPalindrome(int(number))
