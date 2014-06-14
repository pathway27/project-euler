#!/usr/bin/env python

import timeit


def time_func(func):
    def wrapper(*args, **kwargs):
        print func, args, kwargs
        # print timeit.timeit(func,
        #                    setup="from __main__ import first; gc.enable()",
        #                    number=loops)
    return wrapper
