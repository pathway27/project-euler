#!/usr/bin/env/ python
"""
The following iterative sequence is defined for the set of positive integers
 n -> n/2 (n is even)
 n -> 3n + 1 (n is odd)
 
 Using the rule above and starting with 13, we generate the following sequence:
 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
 
It can be seen that this sequence (starting at 13 and fiinishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting 
numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million. 

TODO: Add threads/multiproc
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
    biggest_list = []
    i = 13
    while i < 1000000:
        a = collatz(i, 1)
        b = a.next()
        #print i
        if len(b) > len(biggest_list):
            biggest_list = b
        i += 1

    print len(biggest_list), biggest_list


if __name__ == "__main__":
    print first()