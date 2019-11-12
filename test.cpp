
#include "aux.cpp"
#include "1252.cells-with-odd-values-in-a-matrix.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	int n=2, m=3; 
	vector<vector<int>> ids {{0, 1}, {1,1}};
	say(s.oddCells(n,m,ids));
	return 0;
}

