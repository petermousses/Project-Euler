"""
	In the 20x20 grid below, four numbers along a diagonal line have been marked in red.
	The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
	What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?
"""
row1 =	"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
row2 =	"49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
row3 =	"81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
row4 =	"52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
row5 =	"22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"
row6 =	"24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
row7 =	"32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
row8 =	"67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
row9 =	"24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
row10 =	"21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"
row11 =	"78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
row12 =	"16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
row13 =	"86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
row14 =	"19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
row15 =	"04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"
row16 =	"88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
row17 =	"04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
row18 =	"20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
row19 =	"20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
row20 =	"01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

greatest_product = 0

def makeDataStruct():
	l = list()
	l.append(row1.split(' '))
	l.append(row2.split(' '))
	l.append(row3.split(' '))
	l.append(row4.split(' '))
	l.append(row5.split(' '))
	l.append(row6.split(' '))
	l.append(row7.split(' '))
	l.append(row8.split(' '))
	l.append(row9.split(' '))
	l.append(row10.split(' '))
	l.append(row11.split(' '))
	l.append(row12.split(' '))
	l.append(row13.split(' '))
	l.append(row14.split(' '))
	l.append(row15.split(' '))
	l.append(row16.split(' '))
	l.append(row17.split(' '))
	l.append(row18.split(' '))
	l.append(row19.split(' '))
	l.append(row20.split(' '))
	return l

def getProduct(l, num, row, col) -> int:
	product = 1
	for offset in range(num):
		product *= int(l[row + offset][col + offset])
	return product
def getProductRev(l, num, row, col) -> int:
	product = 1
	for offset in range(num):
		product *= int(l[row - offset][col - offset])
	return product
def getProductUpsideDown(l, num, row, col) -> int:
	product = 1
	for offset in range(num):
		product *= int(l[row - offset][col - offset])
	return product
def getProductRevUpsideDown(l, num, row, col) -> int:
	product = 1
	for offset in range(num):
		product *= int(l[row + offset][col - offset])
	return product
def getProductUp(l, num, row, col) -> int:
	product = 1
	for offset in range(num):
		product *= int(l[row + offset][col])
	return product
def getProductDown(l, num, row, col) -> int:
	product = 1
	for offset in range(num):
		product *= int(l[row - offset][col])
	return product
def getProductRight(l, num, row, col) -> int:
	product = 1
	for offset in range(num):
		product *= int(l[row][col + offset])
	return product
def getProductLeft(l, num, row, col) -> int:
	product = 1
	for offset in range(num):
		product *= int(l[row][col - offset])
	return product

def findDiagonalProduct(num) -> int:
	global greatest_product
	l = makeDataStruct()
	print(getProduct(l, num, 6, 8)) # 1788696
	for row in range(num - 1, len(l) - num):
		for col in range(num - 1, len(l) - num):
			prod = getProduct(l, num, row, col)
			if prod > greatest_product: greatest_product = prod
			prod = getProductRev(l, num, row, col)
			if prod > greatest_product: greatest_product = prod
			prod = getProductUpsideDown(l, num, row, col)
			if prod > greatest_product: greatest_product = prod
			prod = getProductRevUpsideDown(l, num, row, col)
			if prod > greatest_product: greatest_product = prod
			prod = getProductUp(l, num, row, col)
			if prod > greatest_product: greatest_product = prod
			prod = getProductDown(l, num, row, col)
			if prod > greatest_product: greatest_product = prod
			prod = getProductRight(l, num, row, col)
			if prod > greatest_product: greatest_product = prod
			prod = getProductLeft(l, num, row, col)
			if prod > greatest_product: greatest_product = prod

def main():
	print("UNSOLVED")
	findDiagonalProduct(4)
	print(greatest_product)
if __name__ == '__main__': main()