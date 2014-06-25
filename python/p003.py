"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
def factor(n):
	a = []
	upper_limit = int(n**0.5)+1
	for i in range(1, upper_limit):
		if not n % i:
			a.append(i)
			a.append(n // i)
	return a

def prime(n):
	a = factor(n)
	if len(a) == 2: return True
	else: 			return False

def first():
	#print factor(13195)
	a = []
	for fac in factor(600851475143):
		if prime(fac):
			a.append(fac)
	return max(a)

if __name__ == "__main__":
	print factor(600851475143), first()
	import timeit
	print timeit.timeit("first",
                        setup="from __main__ import %s" % ("first"),
                        number=500000)