#!/usr/bin/env/ python
"""
"""

def collatz(start, end):
    a = []
    while start != end:
        a.append(start)
        if start % 2 == 0:
            start = start / 2
        elif start % 2 == 1:
            start = (3 * start) + 1
    if start == end:
        a.append(1)
        yield a

def first():
    big_list = []
    i = 13
    while i < 1000000:
        a = collatz(i, 1)
        b = a.next()
        print i
        big_list.append(b)
        i += 1


if __name__ == "__main__":
    print first()