
#include "aux.cpp"
#include "1301.number-of-paths-with-max-score.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs board = {"E11345","X452XX","3X43X4","44X312","23452X","1342XS"};
	say(s.pathsWithMaxScore(board));
	return 0;
}

