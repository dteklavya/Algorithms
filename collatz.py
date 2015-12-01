#!/usr/bin/env python
'''

'''

import sys
res = []
rstr = ""


def collatz(n):
    global res, rstr
    if n == 1:
        return str(n)
    res.append(str(n))
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    if n > 1:
        return collatz(n)
    else:
        # All elements found, time to create the result string
        res.append(str(n))
        rstr = res[0]
        if res[1:-1]:
            rstr = rstr + "->" + "->".join(res[1:-1])
        if res[-1]:
            rstr = rstr + "->" + res[-1]
        res = []
        return rstr


print collatz(int(sys.argv[1]))
