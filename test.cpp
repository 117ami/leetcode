
#include "aux.cpp"
#include "1588.sum-of-all-odd-length-subarrays.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<int> arr = {1,4,2,5,3} ;

	// std::vector<int> arr = {1,2} ;
	// std::vector<int> arr = {10,11,12} ;
	say(s.sumOddLengthSubarrays(arr));



	return 0;
}

