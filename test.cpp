
#include "aux.cpp"
#include "283.move-zeroes.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi nums = {0, 0, 1};
	nums = {0,1,0,3,12};
	s.moveZeroes(nums); 
	say(nums);
	return 0;
}

