#!/usr/bin/env python
'''

'''


def isodd(number):
    return number & 1


def iseven(number):
    return not number & 1


def find_outlier(array):
    odd, even = 0, 0
    for i in array[:3]:
        if isodd(i):
            odd = odd + 1
        else:
            even = even + 1
    if odd > even:
        for i in array:
            return filter(iseven, array)[0]
    if even > odd:
        for i in array:
            return filter(isodd, array)[0]


print find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
print find_outlier([160, 3, 1719, 19, 11, 13, -21])
