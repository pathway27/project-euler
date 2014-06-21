"""
Find the 10001st prime.

"""

from p3 import prime

def first():
	primes = []
	i = 1
	while len(primes) != 10001:
		if prime(i):
			primes.append(i)
		i += 1

	return len(primes), primes[-1]

def main():
	#prime(30)
	print first()

if __name__ == '__main__':
	main()