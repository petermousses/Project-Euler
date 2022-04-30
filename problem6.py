"""
	The sum of the squares of the first ten natural numbers is,
		1^2 + 2^2 + ... + 10^2 = 385
	The square of the sum of the first ten natural numbers is,
		(1 + 2 + ... + 10)^2 = 55^2 = 3025
	Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
		3025 - 385 = 2640
	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from functools import cache

@cache
def sumOfSquares(num) -> int:
	sum = 0
	for nat_num in range(num + 1):
		sum += nat_num**2
	return sum

@cache
def squareOfSum(num):
	sum = 0
	for nat_num in range(num + 1):
		sum += nat_num
	return sum**2

def main():
	num_to_run = 100
	first = sumOfSquares(num_to_run)
	second = squareOfSum(num_to_run)
	print(first)
	print(second)
	print(second - first)
if __name__ == '__main__': main()