
#include "aux.cpp"
#include "1232.check-if-it-is-a-straight-line.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> cs = {{1, 2}, {2, 3}, {3, 4}, {4, 5}};
	bool res = s.checkStraightLine(cs);
	say(res);
	return 0;
}

