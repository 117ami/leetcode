
#include "aux.cpp"
#include "398.random-pick-index.cpp"

int main(int argc, char const *argv[]) {
	vector<int> nums = {1, 2, 3, 3, 2, 1, 3} ;

	Solution s(nums);
	say(s.pick(3));
	return 0;
}

