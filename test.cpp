
#include "aux.cpp"
#include "18.4sum.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> nums = {1, 0, -1, 0, -2, 2}; 
	vector<vector<int>> res = s.fourSum(nums, 0);
	say(res);
	return 0;
}

