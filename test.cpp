
#include "aux.cpp"
#include "1458.max-dot-product-of-two-subsequences.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> nums1 = {-1,-1}, nums2 = {1,1};
	say(s.maxDotProduct(nums1, nums2));
	return 0;
}

