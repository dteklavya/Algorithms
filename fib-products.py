#!/usr/bin/python

import sys
from math import sqrt


def productFib(prod):
    print "Test case: ", prod
    a, b = 0, 1
    pivot = a * b
    while prod > pivot:
        a, b = b, a + b
        pivot = a * b

    return [a, b, prod == pivot]


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
Test Passed
Test case: 203023208030065646654504166904697594722575
Test Passed
Test case: 203023208030065646654504166904697594722576
Test Passed
Random Tests0
Test case: 7677619978602
Test Passed
Random Tests1
Test case: 507544127
Test Passed
Random Tests2
Test case: 28284465
Test Passed
Random Tests3
Test case: 7677619978602
Test Passed
Random Tests4
Test case: 137769300517680
Test Passed
Random Tests5
Test case: 10803704
Test Passed
Random Tests6
Test case: 944284833567073
Test Passed
Random Tests7
Test case: 9107509825
Test Passed
Random Tests8
Test case: 87841
Test Passed
Random Tests9
Test case: 360684711361584
Test Passed
'''
