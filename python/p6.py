"""
What is the difference between the sum of the squares 
and the square of the sums?


"""

def first():
	sum_of_squares = sum([x**2 for x in range(1, 101)])
	square_of_sums = sum(range(1, 101))**2
	return abs(sum_of_squares - square_of_sums)

def main():
	print first()

if __name__ == '__main__':
	main()