"""
What is the smallest number divisible by each of the 
numbers 1 to 20?

"""

from p3 import factor
import itertools

from fractions import gcd

def lcm(numbers):
    return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)

def first():
	print lcm(range(1, 21))

def main():
	first()

if __name__ == '__main__':
	main()