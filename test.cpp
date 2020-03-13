
#include "aux.cpp"
#include "1368.minimum-cost-to-make-at-least-one-valid-path-in-a-grid.cpp"

int main(int argc, char const *argv[]) {
	string x = "[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]";
	vvi grid = extractMatrixFromString(x);
	Solution s;
	say(s.minCost(grid));
	return 0;
}

