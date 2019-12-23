
#include "aux.cpp"
#include "547.friend-circles.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "[[1,1,0], [1,1,0], [0,0,1]]";
	ss ="[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]";
	vvi m = extractMatrixFromString(ss);
	say(m);
	say(s.findCircleNum(m));
	return 0;
}

