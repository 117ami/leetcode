
#include "aux.cpp"
#include "1473.paint-house-iii.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> h = {0,2,1,2,0}; 
	vector<vector<int>> cost = {{1,10},{10,1},{10,1},{1,10},{5,1}};
	say(s.minCost(h, cost, 5, 2, 3));
	return 0;
}

