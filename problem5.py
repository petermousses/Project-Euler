"""
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def checkDivisibility(num, largest_divisor) -> bool:
	for divisor in range(largest_divisor, 0, -1):
		if num % divisor != 0: return False
	return True

def smallestPositiveNumByDivisorHelper(start_num, largest_divisor) -> int:
	num = start_num
	while True:
		if checkDivisibility(num, largest_divisor): return num
		num += 1

def smallestPositiveNumByDivisor(largest_divisor):
	previous_result = 1
	for num in range(largest_divisor):
		previous_result = smallestPositiveNumByDivisorHelper(previous_result, num)
		print(previous_result)

def main():
	print(smallestPositiveNumByDivisor(20))
if __name__ == '__main__': main()