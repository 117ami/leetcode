
#include "aux.cpp"
#include "1260.shift-2d-grid.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> grid = {{1,2,3},{4,5,6}, {7,8,9}};
	int k = 1; 
	vector<vector<int>> res = s.shiftGrid(grid, k);
	say(res);
	return 0;
}

