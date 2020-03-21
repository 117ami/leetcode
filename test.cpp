
#include "aux.cpp"
#include "947.most-stones-removed-with-same-row-or-column.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	// vvi ss = extractMatrixFromString("[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]");
	string xss = "[[0,0],[0,2],[1,1],[2,0],[2,2]]";
	vvi ss = extractMatrixFromString(xss);
	say(s.removeStones(ss));
	return 0;
}

