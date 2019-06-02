
#include "aux.cpp"
#include "c.cpp"
#include "215.kth-largest-element-in-an-array.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	VI nums = {3,2,3,1,2,4,5,5,6};
	say(s.findKthLargest(nums, 4));
	return 0;
}

