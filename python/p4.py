"""

"""
from p3 import factor

def first():
	a = []
	for i in range(100, 1000):
		for j in range(100, 1000):
			mul = i * j
			if str(mul) == str(mul)[::-1]:
				a.append(mul)

	return max(a)

def main():
	print first()

if __name__ == '__main__':
	main()