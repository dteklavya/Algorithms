#!/usr/bin/env python
'''

'''

import sys


def cat_digits(digits):
    number = 0
    for index, digit in enumerate(digits):
        number = number + (digit * (10 ** index))
    return number


def next_bigger(number):
    digits = []
    tail = 1
    while(number > 0):
        number, tail = divmod(number, 10)
        digits.append(tail)
    for index, digit in enumerate(digits):
        for i in range(index + 1, len(digits)):
            if digit > digits[i]:
                digits[index], digits[i] = digits[i], digits[index]
                digits[0:i] = reversed(digits[0:i])
                return cat_digits(digits)
    return -1

print next_bigger(int(sys.argv[1]))
