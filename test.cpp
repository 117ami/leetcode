
#include "aux.cpp"
#include "1130.minimum-cost-tree-from-leaf-values.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi arr {7, 12, 8, 10, 6};
	arr = {6,2,4};
	say(s.mctFromLeafValues(arr));
	return 0;
}

