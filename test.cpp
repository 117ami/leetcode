
#include "aux.cpp"

#include "1567.maximum-length-of-subarray-with-positive-product.cpp"

int main(int argc, char const *argv[]) {
  Solution s;
  std::vector<int> nums = {1, -2, -3, 4};

  // std::vector<int> nums = {0,1,-2,-3,-4} ;

  // std::vector<int> nums = {-1,-2,-3,0,1} ;

  // std::vector<int> nums = {-1,2} ;

  // std::vector<int> nums = {1,2,3,5,-6,4,0,10} ;
  nums = {16, 0, 5, 2, 2, 13, 11, 8};
//   nums = {-1, 2};
	nums = {-16,0,-5,2,2,-13,11,8};
  say(s.getMaxLen(nums));

  return 0;
}
