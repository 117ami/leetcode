#include <iostream>
#include <stdio.h>
#include <vector>

/**
   Your are given an array of positive integers nums.
   Count and print the number of (contiguous) subarrays where the product of all
   the elements in the subarray is less than k.
   Example 1:
   Input: nums = [10, 5, 2, 6], k = 100
   Output: 8
   Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
   [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
   Note that [10, 5, 2] is not included as the product of 100 is not strictly
less
   than k.
   Note:
   0 < nums.length <= 50000.
   0 < nums[i] < 1000.
   0 <= k < 10^6.

**/

using namespace std;
class Solution {
public:
  int numSubarrayProductLessThanK(vector<int> &nums, int k) {
    unsigned int i, left = 0, res = 0;
    int product = 1;
    for (i = 0; i < nums.size(); i++) {
      product *= nums[i];
      while (product >= k && left <= i) {
        product /= nums[left];
        left++;
      }
      res += (i - left + 1);
    }
    return res;
  }

  int numSubarrayProductLessThanK2(vector<int> &nums, int k) {
    if (k <= 1)
      return 0;
    int size = (int)nums.size();
    int *pi = &nums[0], *pe = pi + size, *ps = pi, res = 0, product = 1;
    while (pi < pe) {
      product *= *pi++;
      while (product >= k) {
        product /= *ps++;
      }
      res += (int)(pi - ps);
    }
    return res;
  }
};

int main() {
  Solution s;
  //  vector<int> nums{10, 5, 2, 6, 3, 2, 1, 1, 100, 3};
  vector<int> nums{1, 1, 1};
  int k = 1;
  cout << s.numSubarrayProductLessThanK(nums, k) << endl;
  cout << s.numSubarrayProductLessThanK2(nums, k) << endl;
}
