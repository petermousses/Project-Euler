# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
functionCallCounter = 1

def isPrime(n) -> bool:
	global functionCallCounter
	if n <= 3: return n > 1
	if not n%2 or not n%3: return False
	i = 5
	while i <= int(n**0.5):
		if not n%i or not n%(i + 2):
			return False
		i += 6
	functionCallCounter += 1
	print(n)
	return True

def main():
	num_to_call = 10001
	num = 2
	while functionCallCounter < num_to_call - 1:
		if isPrime(num):
			print(num)
		num += 1
if __name__ == '__main__': main()