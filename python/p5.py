"""
What is the smallest number divisible by each of the 
numbers 1 to 20?

"""

from p3 import factor
import itertools

# Generator with yield
def multiples(n):
	num = 1
	while True:
		yield n * num
		num += 1

def imerge(a, b):
    for i, j in itertools.izip(a,b):
        yield i
        yield j

def first():
	three = itertools.count(1, 6)
	four = itertools.count(1, 4)
	t_f = three + four
	print three.next()
	#four = multiples(4)
	

def main():
	first()

if __name__ == '__main__':
	main()