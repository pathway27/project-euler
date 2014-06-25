#!/usr/bin/env/ python


def fib_re(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_re(n-1) + fib_re(n-2)

def fib(n):
    f = [1, 2]
    for x in xrange(2, n):
        f.append(f[x-2] + f[x-1])
    return f

def first():
    return sum([x for x in fib(100) if x < (4 * 10 ** 6) and
            not x % 2])

if __name__ == "__main__":
    print first()