/*
 * @lc app=leetcode id=152 lang=cpp
 *
 * [152] Maximum Product Subarray
 *
 * https://leetcode.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (29.27%)
 * Total Accepted:    211.5K
 * Total Submissions: 722.5K
 * Testcase Example:  '[2,3,-2,4]'
 *
 * Given an integer array nums, find the contiguous subarray within an array
 * (containing at least one number) which has the largest product.
 *
 * Example 1:
 *
 *
 * Input: [2,3,-2,4]
 * Output: 6
 * Explanation: [2,3] has the largest product 6.
 *
 *
 * Example 2:
 *
 *
 * Input: [-2,0,-1]
 * Output: 0
 * Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 *
 */
using namespace std;
using LL = long long;

class Solution {
public:
  int maxProduct(vector<int> &nums) {
    int imax = 1, imin = 1, res = nums[0];
    for (int &n : nums) {
      if (n < 0)
        swap(imax, imin);
      imax = max(imax * n, n);
      imin = min(imin * n, n);
      res = max(imax, res);
    }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
