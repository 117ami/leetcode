#include "aux.cpp"
#include "1277.count_square_submatrices_with_all_ones.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> matrix = {{0,1,1,1}, {1,1,1,1}, {0,1,1,1}};
	matrix = {{0,0,0},{0,1,0},{0,1,0},{1,1,1},{1,1,0}};
	int i = s.countSquares(matrix);
	cout << i << endl; 
	return 0;
}

