
#include "aux.cpp"
#include "c.cpp"
#include "1072.flip-columns-for-maximum-number-of-equal-rows.cpp"

int main(int argc, char const *argv[]) {
	Solution s;

	VVI matrix={{0,0,0},{0,0,1},{1,1,0}};
	matrix = {{0,1,0,1},{1,1,1,1},{1,0,1,1},{0,0,1,1},{0,1,0,0},{1,1,0,1},{1,0,0,0},{1,0,1,1},{0,0,1,1},{1,0,1,1}};

	say(s.maxEqualRowsAfterFlips(matrix));
	return 0;
}

