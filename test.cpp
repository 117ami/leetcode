
#include "aux.cpp"
#include "153.find-minimum-in-rotated-sorted-array.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<int> nums = {2, 3, 4, 5, 6, 1};
	int res = s.findMin(nums);
	say(res);
	return 0;
}

