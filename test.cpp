
#include "aux.cpp"
#include "1519.number-of-nodes-in-the-sub-tree-with-the-same-label.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi edges = {{0, 2}, {0, 3}, {1, 2}}; 
	say(s.countSubTrees(4, edges, "aeed"));
	return 0;
}

