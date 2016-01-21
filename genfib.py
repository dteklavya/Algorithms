#!/usr/bin/env python


def genfib():
    global p, n
    p, n = 0, 1

    def fibn():
        global p
        global n
        while True:
            f = p
            p, n = n, p + n
            yield f

    global f
    f = fibn()

    def fib():
        global f
        return f.next()
    return fib


fb = genfib()
print fb()
print fb()
print fb()
print fb()
print fb()
print fb()
print fb()
