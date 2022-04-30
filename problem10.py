"""
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	Find the sum of all the primes below two million.
"""
def isPrime(n) -> bool:
	if n <= 3: return n > 1
	if not n % 2 or not n % 3: return False
	i = 5
	while i <= int(n**0.5):
		if not n % i or not n % (i + 2):
			return False
		i += 6
	#print(n)
	return True

def main():
	print(sum(num for num in range(2000000) if isPrime(num)))
if __name__ == '__main__': main()