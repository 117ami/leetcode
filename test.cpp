
#include "aux.cpp"
#include "934.shortest-bridge.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> a = {{0,1,0},{0,0,0},{0,0,1}};
	a = {{1,1,1,1,1},{1,0,0,0,1},{1,0,1,0,1},{1,0,0,0,1},{1,1,1,1,1}};
	say(s.shortestBridge(a));
	return 0;
}

