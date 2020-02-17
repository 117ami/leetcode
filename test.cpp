
#include "aux.cpp"
#include "1354.construct-target-array-with-multiple-sums.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi target = {3,5,9};
	target = {1,49,11,1,25,1,7};
	target = {9,3,5};
	say(s.isPossible(target));
	return 0;
}

