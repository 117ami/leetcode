
#include "aux.cpp"
#include "1558.minimum-numbers-of-function-calls-to-make-target-array.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<int> nums = {1,5} ;
	nums = {2,2} ;
	nums = {4,2,5} ;
	// nums = {3,2,2,4} ;
	// nums = {2,4,8,16} ;
	say(s.minOperations(nums));
	return 0;
}

