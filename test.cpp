
#include "aux.cpp"
#include "1569.number-of-ways-to-reorder-array-to-get-same-bst.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<int> 
	nums = {2,1,3} ;
	nums = {3,4,5,1,2} ;
	nums = {1,2,3} ;
	nums = {3,1,2,5,4,6} ;
	nums = {9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18} ;
	say(s.comb(10000, 3580));
	say(s.numOfWays(nums));


	return 0;
}

