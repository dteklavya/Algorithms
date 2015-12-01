#!/usr/bin/env python
'''

'''

import sys


def memoize(fn):
    def alias(args):
        if args not in alias.cache:
            alias.cache[args] = fn(args)
        return alias.cache[args]
    alias.cache = {}
    return alias


@memoize
def collatz(number):
    if number == 1:
        return 1
    if number % 2:
        count = collatz(number * 3 + 1)
    else:
        count = collatz(number / 2)
    return count + 1


def max_collatz_length(number):
    if number < 1 or not type(number) is int:
        return []
    counts = {}
    stop = number / 2 + 1
    if number == 1:
        stop = 2
    for i in xrange(1, stop):
        counts[i] = collatz(i)
        if i * 2 <= number:
            counts[i * 2] = counts[i] + 1
    if not number % 2:
        number = number - 1
    for i in xrange(number, stop - 1, -2):
        counts[i] = collatz(i)

    winner = max(counts, key=counts.get)
    return [winner, counts[winner]]


print "Result: ", max_collatz_length(sys.argv[1])

assert max_collatz_length(0) == []
assert max_collatz_length(1) == [1, 1]
assert max_collatz_length(4) == [3, 8]
assert max_collatz_length('a') == []
assert max_collatz_length(23) == [18, 21]


'''

Test Cases from Codewars

Simple tests
should handle basic values
Test Passed
Test Passed
Test Passed
Test Passed
should handle big values
Test Passed
Test Passed
Error tests
should handle basic values
Test Passed
Test Passed
Test Passed
Test Passed
Random tests
Testing for 8544
Test Passed
Testing for 2141
Test Passed
Testing for 174973
Test Passed
Testing for 1054
Test Passed
Testing for 10937
Test Passed
Testing for 6093
Test Passed
Testing for 686
Test Passed
Testing for 988
Test Passed
Testing for 42665
Test Passed
Testing for 10
Test Passed
Testing for 1496
Test Passed
Testing for 2508
Test Passed
Testing for 74
Test Passed
Testing for 1662
Test Passed
Testing for 170014
Test Passed
Testing for 1113
Test Passed
Testing for 196
Test Passed
Testing for 85096
Test Passed
Testing for 16649
Test Passed
Testing for 116
Test Passed
Testing for 18919
Test Passed
Testing for 7
Test Passed
Testing for 2664
Test Passed
Testing for 116801
Test Passed
Testing for 63321
Test Passed
Testing for 1989
Test Passed
Testing for 18
Test Passed
Testing for 141114
Test Passed
Testing for 23
Test Passed
Testing for 100
Test Passed
Testing for 174
Test Passed
Testing for 61953
Test Passed
Testing for 127847
Test Passed
Testing for 59
Test Passed
Testing for 101540
Test Passed
Testing for 17
Test Passed
Testing for 13136
Test Passed
Testing for 157
Test Passed
Testing for 14
Test Passed
Testing for 37
Test Passed
50 Passed
0 Failed
0 Errors

Process took 4905ms to complete

'''
