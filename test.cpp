
#include "aux.cpp"
#include "457.circular-array-loop.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi nums = {2, -1, 1, 2, 2};
	// nums = {-2, 1, -1, -2, -2};
	// nums = {-1, -2, -3, -4, -5};
	// nums = {-1,2,1,2};
	vi copy(nums);
	say(s.circularArrayLoop(nums));
	say(s.circularArrayLoop_2(copy));
	return 0;
}

