#!/usr/bin/env python2

n = 100


def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n-1)
        fib.append(fib[-2] + fib[-1])
        return fib

for f in fibonacci(n):
    print f
