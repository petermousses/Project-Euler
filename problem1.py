"""
	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	
	Find the sum of all the multiples of 3 or 5 below 1000.
"""
def doMath(end, divisor) -> int:
	n = (end - 1) // divisor
	return divisor * n * (n + 1) // 2

def getSumForDivisor(end = 1000) -> int:
	return doMath(end, 3) +  doMath(end, 5) -  doMath(end, 15)

def main():
	print(getSumForDivisor())
if __name__ == '__main__': main()
