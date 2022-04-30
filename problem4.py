"""
	A palindromic number reads the same both ways.
	The largest palindrome made from the product of two 2-digit numbers is 
		9009 = 91 x 99.
	Find the largest palindrome made from the product of two 3-digit numbers.
"""
def isPalindrome(num) -> bool:
	initialStrArr = list(str(num))
	reverseStrArr = []
	for reverse_index in range(len(initialStrArr) - 1, -1, -1):
		reverseStrArr.append(initialStrArr[reverse_index])
	if (int(''.join(initialStrArr))) != (int(''.join(reverseStrArr))): return False
	return True

def generatePalindromes(digit_len) -> tuple:
	max_palindrome_product = 0
	operand1 = 0
	operand2 = 0
	for num1 in range(10**(digit_len - 1), 10**(digit_len)):
		for num2 in range(num1, 10**(digit_len)):
			product = num1 * num2
			if isPalindrome(product) and product >= max_palindrome_product:
				operand1 = num1
				operand2 = num2
				max_palindrome_product = product
	return operand1, operand2, max_palindrome_product

def main():
	nums = generatePalindromes(3)
	print(f"{nums[0]} * {nums[1]} = {nums[2]}")
if __name__ == '__main__': main()