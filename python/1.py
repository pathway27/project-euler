#!/usr/bin/env/ python


def first():
    sum = 0
    for x in range(1, 1000):
        if not x % 3 or not x % 5:
            sum += x
    return sum


def second():
    return sum([i for i in range(1, 1000) if not i % 5 or not i % 3])

if __name__ == "__main__":
    import timeit
    print timeit.timeit("first()", setup="from __main__ import first",
                        number=10000)
    print timeit.timeit("second()", setup="from __main__ import second",
                        number=10000)
