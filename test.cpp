
#include "aux.cpp"
#include "1526.minimum-number-of-increments-on-subarrays-to-form-a-target-array.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi target = {3,1,5,4,2};
	say(s.minNumberOperations(target));
	return 0;
}

