
#include "aux.cpp"
#include "310.minimum-height-trees.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	int n = 6;
	vvi edges = {{0, 3}, {1, 3}, {2, 3}, {4, 3}, {5, 4}};
	vi res = s.findMinHeightTrees(n, edges);
	say(res);
	return 0;
}

