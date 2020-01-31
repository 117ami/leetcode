
#include "aux.cpp"
#include "1329.sort-the-matrix-diagonally.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi mat = extractMatrixFromString("[[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]");
	vvi res = s.diagonalSort(mat);
	say(res);
	return 0;
}

