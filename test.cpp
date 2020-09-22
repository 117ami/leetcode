
#include "aux.cpp"
#include "1589.maximum-sum-obtained-of-any-permutation.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	// std::vector<int> nums = {1,2,3,4,5} ;
	// std::vector<vector<int>> requests = {{1,3},{0,1}} ;
	// std::vector<int> nums = {1,2,3,4,5,6} ;
	// std::vector<vector<int>> requests = {{0,1}} ;
	std::vector<int> nums = {1,2,3,4,5,10} ;
	std::vector<vector<int>> requests = {{0,2},{1,3},{1,1}} ;
	say(s.maxSumRangeQuery(nums,requests));



	return 0;
}

