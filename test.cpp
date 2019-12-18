
#include "aux.cpp"
#include "1202.smallest-string-with-swaps.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string st = "dcab";
	vvi pairs = {{0, 3}, {1, 2}, {0, 2}} ;
	st = "dcab", pairs = {{0,3}, {1, 2}};
	say(s.smallestStringWithSwaps(st, pairs));
	return 0;
}

