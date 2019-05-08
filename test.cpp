
#include "aux.cpp"
#include "1.two-sum.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<int> nums = {1, 2, 3, 7, 3, 7, 19};
	int target = 6; 
	say(s.twoSum(nums, target));
	return 0;
}

