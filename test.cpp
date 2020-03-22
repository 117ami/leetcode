
#include "aux.cpp"
#include "1389.create-target-array-in-the-given-order.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi nums = {0,1,2,3,4}, index = {0,1,2,2,1}; 
	say(s.createTargetArray(nums, index));
	return 0;
}

