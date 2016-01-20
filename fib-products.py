#!/usr/bin/python

import sys
from math import sqrt


def memoize(fn):
    cache = dict()
    def wrap(*a):
        key = tuple(a)
        if key not in cache:
            cache[key] = fn(*a)
        return cache[key]
    return wrap


@memoize
def is_fibonacci(n):
    prod = 5 * (n ** 2)
    num1 = prod + 4
    case1 = int(sqrt(num1))
    if case1 ** 2 == num1:
        return True

    num2 = prod - 4
    case2 = int(sqrt(num2))
    if case2 ** 2 == num2:
        return True

    return False


def memfibs(fn):
    cache = dict()
    def wrap(*a):
        key = tuple(a)
        if key not in cache:
            cache[key] = fn(*a)
        return cache[key]
    return wrap

@memfibs
def get_fibs(n):
    prev = int(round(n / 1.6))
    next = int(round(n * 1.6))
    while not is_fibonacci(prev):
        prev = prev + 1
    while not is_fibonacci(next):
        next = next + 1

    return (prev, next)


def productFib(prod):
    print "Test case: ", prod
    for i in xrange(int(sqrt(prod)), 0, -1):
        if is_fibonacci(i):
            (prevfib, nextfib) = get_fibs(i)
            lower = i * prevfib
            if lower == prod:
                return [i, prevfib, True]
            elif lower < prod:
                upper = i * nextfib
                if upper == prod:
                    return [i, nextfib, True]
                elif upper > prod:
                    return [i, nextfib, False]
                else:
                    (p, n) = get_fibs(nextfib)
                    if nextfib * n > prod:
                        return [nextfib, n, False]
            else:
                continue
        else:
            continue


number = int(sys.argv[1])
print productFib(number)



'''
Test case: 4895
Test Passed
Test case: 5895
Test Passed
Test case: 74049690
Test Passed
Test case: 84049690
Test Passed
Test case: 193864606
Test Passed
Test case: 447577
Test Passed
Test case: 602070
Test Passed
Test case: 602070602070
Test Passed
Test case: 1120149658760
Test Passed
Test case: 256319508074468182850

'''
