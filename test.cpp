
#include "aux.cpp"
#include "1341.the-k-weakest-rows-in-a-matrix.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]";
	vvi mat = extractMatrixFromString(ss);
	say(s.kWeakestRows(mat, 3));
	return 0;
}

