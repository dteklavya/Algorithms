#!/usr/bin/python

import sys


def memoize(fn):
    cache = dict()
    def wrap(*a):
        key = tuple(a)
        if key not in cache:
            cache[key] = fn(*a)
        return cache[key]
    return wrap


@memoize
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


def sum_for_list(numbers):
    result = {}
    negative = 0
    for number in numbers:
        if number < 0:
            number = number * -1
            negative = 1
        print number
        if is_prime(number):
            factors = [number]
        else:
            factors = set(reduce(list.__add__, ([i, number//i]
                        for i in range(2, int(number ** 0.5) + 1)
                            if number % i == 0)))
            factors = filter(is_prime, factors)
        if negative:
            number = number * -1
        for n in factors:
            if n in result:
                result[n] = result[n] + number
            else:
                result[n] = number
    return [[i, result[i]] for i in sorted(result)]


#print sum_for_list([12, 15, 25])
## print sum_for_list(int(sys.argv[1]))
#print sum_for_list([15, 30, -45])
print sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100])


'''

Test cases from codewars

12
15
Test Passed
15
21
24
30
45
Test Passed
15
21
24
30
45
Test Passed
107
158
204
100
118
123
126
110
116
100
Test Passed
29804
4209
28265
72769
31744
Test Passed
5 Passed
0 Failed
0 Errors

Process took 124ms to complete

'''
