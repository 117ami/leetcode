
#include "aux.cpp"
#include "c.cpp"
#include "886.possible-bipartition.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	VVI dislikes={{1,2},{1,3},{2,4}};
	dislikes = {{1,2},{2,3},{3,4},{4,5},{1,5}};
	say(s.possibleBipartition(5,dislikes));
	return 0;
}

