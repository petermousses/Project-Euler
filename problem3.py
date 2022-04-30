"""
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?
"""
def isPrime(n) -> bool:
	if n <= 3: return n > 1
	if not n % 2 or not n % 3: return False
	for i in range(5, int(n**0.5) + 1, 6):
		if not n % i or not n % (i + 2): return False
	return True

def findLargestPrimeFactor(largestPrimeFactor, num = 600851475143):
	for x in range(num - 1):
		if isPrime(x) and num % x == 0:
			largestPrimeFactor = x
			print(largestPrimeFactor)

def main():
	largestPrimeFactor = findLargestPrimeFactor(0)
	print(largestPrimeFactor)
if __name__ == '__main__': main()