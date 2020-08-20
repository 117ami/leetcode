
#include "aux.cpp"
#include "815.bus-routes.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> ns = {{1, 3, 7}, {2, 4, 8}, {2, 5, 7}};
	say(s.numBusesToDestination(ns, 1, 4));
	return 0;
}

