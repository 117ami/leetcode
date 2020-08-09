
#include "aux.cpp"
#include "1547.minimum-cost-to-cut-a-stick.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi cuts = {5,6,1,4,2};
	say(s.minCost(9, cuts));
	return 0;
}

