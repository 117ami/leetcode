
#include "aux.cpp"
#include "c.cpp"
#include "1074.number-of-submatrices-that-sum-to-target.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	VVI matrix = {{0, 1, 0}, {1,1,1},{0,1,0}};
	say(s.numSubmatrixSumTarget(matrix, 3));
	return 0;
}

