"""
	Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
	How many such routes are there through a 20x20 grid?
"""
class Node:
	def __init__(self, dataval=0, r=None, d=None):
		self.right = r
		self.down = d
	
	def print(self):
		print("[]")

class Grid:
	def __init__(self, size):
		self.head = Node()
		self.size = size
		iter1 = self.head
		iter2 = self.head
		if size > 1:
			for _ in range(0, size):
				iter1 = iter2
				for _ in range(0, size):
					iter1.right = Node()
					iter1 = iter1.right
				iter2.down = Node()
				iter2 = iter2.down
	
	def print(self):
		iter = self.head
		for _ in range(0, self.size):
			print("row")
			for _ in range(0, self.size):
				print("col")
				iter.print()
				iter = iter.right
			print()
			iter = iter.down

def traverse(dim):
	grid = Grid(dim)
	grid.print()

def main():
	traverse(2)
if __name__ == '__main__': main()