#include <stdio.h>
/**
Given an integer array&nbsp;nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.
Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation:&nbsp;[2,3] has the largest product 6.
Example 2:
Input: [-2,0,-1]
Output: 0
Explanation:&nbsp;The result cannot be 2, because [-2,-1] is not a subarray.

**/

#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

auto speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(nullptr);
  return nullptr;
}();

class Solution {
public:
  int maxProduct(vector<int> &nums) {
    if (nums.size() == 1)
      return nums[0];
    int imax = 1, imin = 1, res = 0;
    for (auto n : nums) {
      if (n < 0)
        std::swap(imax, imin);
      imax = n > n * imax ? n : n * imax;
      imin = n > n * imin ? n * imin : n;
      res = res > imax ? res : imax;
    }
    return res;
  }
};

int main() {
  Solution s;
  vector<int> nums{2, 3, -1, 4, -2, 1};
  cout << s.maxProduct(nums) << endl;
  int a = 10, b = 24;
  std::swap(a, b);
  cout << a << ", " << b << endl;
}
