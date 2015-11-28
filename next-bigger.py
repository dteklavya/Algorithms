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
                return cat_digits(digits)
            elif digit < digits[i]:
                digits[index], digits[i] = digits[i], digits[index]
                break
            else:
                break

print next_bigger(int(sys.argv[1]))
