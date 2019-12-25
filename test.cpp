
#include "aux.cpp"
#include "632.smallest-range-covering-elements-from-k-lists.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi nums = extractMatrixFromString("[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]");
	say(s.smallestRange(nums));
	return 0;
}

