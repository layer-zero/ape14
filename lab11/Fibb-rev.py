#!/usr/bin/env python2

n = 100
fib = [0, 1]

for i in range(n-2):
    fib.append(fib[-1]+fib[-2])

for f in reversed(fib):
    print f
