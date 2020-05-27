
#include "aux.cpp"
#include "785.is-graph-bipartite.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> g = {{1,2,3}, {0,2}, {0,1,3}, {0,2}};
	say(s.isBipartite(g));
	return 0;
}

