
#include "aux.cpp"
#include "1577.number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	// std::vector<int> nums1 = {7,4} ;
	// std::vector<int> nums2 = {5,2,8,9} ;

	std::vector<int> nums1 = {1,1} ;
	std::vector<int> nums2 = {1,1,1} ;

	// std::vector<int> nums1 = {7,7,8,3} ;
	// std::vector<int> nums2 = {1,2,9,7} ;
	// nums1={43024,99908}, nums2={1864};
	say(s.numTriplets(nums1,nums2));



	return 0;
}

