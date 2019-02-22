#!/usr/bin/env python2

n = 100


def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n-1)
        fib_list.append(fib_list[-2]+fib_list[-1])
        return fib_list

fib = fibonacci(n)

for f in fib:
    print f
