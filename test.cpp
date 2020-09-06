
#include "aux.cpp"
#include "1574.shortest-subarray-to-be-removed-to-make-array-sorted.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<int> arr = {1,2,3,10,4,2,3,5} ;
	// std::vector<int> arr = {5,4,3,2,1} ;
	// std::vector<int> arr = {1,2,3} ;
	// std::vector<int> arr = {1} ;
	// arr = {13,0,14,7,18,18,18,16,8,15,20};
	// arr ={6,3,10,11,15,20,13,3,18,12};
	say(s.findLengthOfShortestSubarray(arr));



	return 0;
}

