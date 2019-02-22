#!/usr/bin/env python2

n = 100
# This is a good application for tuples (n, f), where n is the sequence number
# and f is the corresponding fibonacci number.
fib = [(1, 0), (2, 1)]

for i in range(3, n+1):
    fib.append((i, fib[-1][1]+fib[-2][1]))

for f in reversed(fib):
    print str(f[0]) + ': ' + str(f[1])
