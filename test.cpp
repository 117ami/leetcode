
#include "aux.cpp"
#include "1042.flower-planting-with-no-adjacent.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> paths = {{1, 2}, {2, 3}, {3, 1}}; 
	say(s.gardenNoAdj(3, paths));
	return 0;
}

