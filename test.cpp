
#include "aux.cpp"
#include "c.cpp"
#include "1091.shortest-path-in-binary-matrix.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi g = {{0,0,0},{1,1,0},{1,1,0}};
	say(s.shortestPathBinaryMatrix(g));
	return 0;
}

