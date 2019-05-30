
#include "aux.cpp"
#include "c.cpp"
#include "330.patching-array.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	VI nums = {1, 5, 10}; 
	say(s.minPatches(nums, 20));
	return 0;
}

