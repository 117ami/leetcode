
#include "aux.cpp"
#include "1343.number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi arr = {11,13,17,23,29,31,7,5,2,3}; 
	// arr = {2,2,2,2,5,5,5,8};
	say(s.numOfSubarrays(arr, 3, 5));
	return 0;
}

