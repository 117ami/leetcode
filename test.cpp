
#include "aux.cpp"
#include "952.largest-component-size-by-common-factor.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> ns = {20,50,9,63};
	// ns={2,3,6,7,4,12,21,39};
	ns = {4,6,15,35};
	ns = {1,2,3,4,5,6,7,8,9};
	// ns = {3,4,5};
	// ns = {99,68,70,77,35,52,53,25,62};
	// ns = {65,35,43,76,15,11,81,22,55,92,31};
	// ns = {865,226,261,780,585,398,194,63,399,853,180,590,54,430,824,949,187,29,62,95};
	say(s.largestComponentSize(ns));
	return 0;
}

