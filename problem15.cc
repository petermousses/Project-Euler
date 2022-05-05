#include <iostream>
#include <string>

class Grid {
	public:
	struct Node {
		Node * right;
		Node * down;
	};
	int size;
	Node * start;
	Grid(int size): size(size) {}
	std::ostream& operator<<(std::ostream& os, const Grid& obj) {

		return os
	}
};

int main() {
	Grid * g = new Grid(2);
	return 0;
}