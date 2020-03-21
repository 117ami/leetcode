
#include "aux.cpp"
#include "947.most-stones-removed-with-same-row-or-column.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi ss = extractMatrixFromString("[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]");
	say(s.removeStones(ss));
	return 0;
}

