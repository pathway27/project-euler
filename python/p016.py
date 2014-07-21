"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sum_pow(n, power):
    p = n ** power
    a = 0
    for i in str(p):
        a += int(i)
    return a 

def first():
    return sum_pow(2, 1000)

if __name__ == "__main__":
    print first()