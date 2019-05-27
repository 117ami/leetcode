
#include "aux.cpp"
#include "1052.grumpy-bookstore-owner.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> c = {1, 0, 1, 2, 1, 1, 7, 5}, g = {0, 1, 0, 1, 0, 1, 0, 1};
	say(s.maxSatisfied(c, g, 3));
	return 0;
}

