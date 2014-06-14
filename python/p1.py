#!/usr/bin/env/ python


def first():
    msum = 0
    for x in range(1, 1000):
        if not x % 3 or not x % 5:
            msum += x
    return msum


def second():
    return sum([i for i in range(1, 1000) if not i % 5 or not i % 3])


def third():
    divs = []
    for x in range(1000):
        if not x % 3 or not x % 5:
            divs.append(x)
    return sum(divs)

if __name__ == "__main__":
    import timeit
    func_list = [locals()[key] for key in locals().keys()
                 if callable(locals()[key])]
    fn_max = max([len(x.__name__) for x in func_list])
    for f in reversed(func_list):
        spaces = (fn_max - len(f.__name__)) * ' '
        print f.__name__ + '()' + spaces + ': ' + str(f()) + ' ',
        print timeit.timeit(f,
                            setup="from __main__ import %s" % (f.__name__),
                            number=5000) / 5000
