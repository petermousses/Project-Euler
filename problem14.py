"""
	The following iterative sequence is defined for the set of positive integers:
		n → n/2 (n is even)
		n → 3n + 1 (n is odd)
	Using the rule above and starting with 13, we generate the following sequence:
		13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
	It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
	Which starting number, under one million, produces the longest chain?
	NOTE: Once the chain starts the terms are allowed to go above one million.
"""
def getChainLength(num):
	chain = 1
	while num > 1:
		num = (num // 2) if (num % 2 == 0) else (3 * num + 1)
		chain += 1
	return chain

def main():
	longest_chain_starting_number = 0
	longest_chain_length = 0
	for num in range(1000000):
		chain_length = getChainLength(num)
		if chain_length >= longest_chain_length: 
			longest_chain_length = chain_length
			longest_chain_starting_number = num
	print(longest_chain_starting_number)
if __name__ == '__main__': main()