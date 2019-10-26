
#include "aux.cpp"
#include "15.3sum.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> nums = {-1, 0, 1, 2, -1, -4};
	vector<vector<int>> res = s.threeSum(nums); 
	say(res);
	return 0;
}

