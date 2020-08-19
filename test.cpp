
#include "aux.cpp"
#include "847.shortest-path-visiting-all-nodes.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> ns ={{1}, {0, 2, 4}, {1, 3, 4}, {2}, {1, 2}};
	say(s.shortestPathLength(ns));
	return 0;
}

