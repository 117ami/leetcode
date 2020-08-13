
#include "aux.cpp"
#include "927.three-equal-parts.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> x = {1, 1, 1, 0, 1, 1, 1, 1, 1, 1};
	// x = {1,0, 1,0,1};
	say(s.threeEqualParts(x));
	return 0;
}

