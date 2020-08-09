
#include "aux.cpp"
#include "1546.maximum-number-of-non-overlapping-subarrays-with-sum-equals-target.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi ns = {-2,6,6,3,5,4,1,2,8}; 
	int n = 10; 
	say(s.maxNonOverlapping(ns, n));
	return 0;
}

