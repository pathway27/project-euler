#!/usr/bin/env/ python
"""
how to do combinations?
"""

def fact(n):
    f = 1
    for x in xrange(1, n+1):
        f = f * x
    return f
 

def first():
    return fact(40) / fact(20) / fact(20)

if __name__ == "__main__":
    print first()