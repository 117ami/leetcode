
#include "aux.cpp"
#include "689.maximum-sum-of-3-non-overlapping-subarrays.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi ns = {7, 13, 20, 19, 19, 2, 10, 1, 1, 19}; 
	int k = 3; 
	ns = {1,2,1,2,6,7,5,1}, k = 2; 
	say(s.maxSumOfThreeSubarrays(ns, k));
	return 0;
}

