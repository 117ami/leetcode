
#include "aux.cpp"
#include "493.reverse-pairs.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi ns = {1,3,2,3,1};
	ns = {2,4,3,5,1};
	// ns = {2147483647,2147483647,2147483647,2147483647,2147483647,2147483647};
	say(s.reversePairs(ns));
	return 0;
}

