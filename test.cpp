
#include "aux.cpp"
#include "1466.reorder-routes-to-make-all-paths-lead-to-the-city-zero.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> tmp = {{1, 0}, {0, 2}};
	say(s.minReorder(3, tmp));
	return 0;
}

