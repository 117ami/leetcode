
#include "aux.cpp"
#include "c.cpp"
#include "719.find-k-th-smallest-pair-distance.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi nums ={1,3,1}; int k = 1;
	say(s.smallestDistancePair(nums, k));
	return 0;
}

