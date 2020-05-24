/*
 * @lc app=leetcode id=1458 lang=cpp
 *
 * [1458] Max Dot Product of Two Subsequences
 *
 * https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/
 *
 * algorithms
 * Hard (37.67%)
 * Total Accepted:    5.2K
 * Total Submissions: 13.7K
 * Testcase Example:  '[2,1,-2,5]\r\n[3,0,-6]\r'
 *
 * Given two arrays nums1 and nums2.
 *
 * Return the maximum dot product between non-empty subsequences of nums1 and
 * nums2 with the same length.
 *
 * A subsequence of a array is a new array which is formed from the original
 * array by deleting some (can be none) of the characters without disturbing
 * the relative positions of the remaining characters. (ie, [2,3,5] is a
 * subsequence of [1,2,3,4,5] while [1,5,3] is not).
 *
 *
 * Example 1:
 *
 *
 * Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
 * Output: 18
 * Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from
 * nums2.
 * Their dot product is (2*3 + (-2)*(-6)) = 18.
 *
 * Example 2:
 *
 *
 * Input: nums1 = [3,-2], nums2 = [2,-6,7]
 * Output: 21
 * Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
 * Their dot product is (3*7) = 21.
 *
 * Example 3:
 *
 *
 * Input: nums1 = [-1,-1], nums2 = [1,1]
 * Output: -1
 * Explanation: Take subsequence [-1] from nums1 and subsequence [1] from
 * nums2.
 * Their dot product is -1.
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums1.length, nums2.length <= 500
 * -1000 <= nums1[i], nums2[i] <= 1000
 *
 */
class Solution {
public:
  int maxDotProduct(vector<int> &A, vector<int> &B) {
    int m = A.size(), n = B.size();
    vector<int> dp(n + 1, -0x3f3f3f3f);
    for (int i = 1; i <= m; i++) {
      vector<int> cc(dp);
      for (int j = 1; j <= n; j++) {
        dp[j] = max(cc[j], dp[j]);
        dp[j] = max(cc[j - 1], dp[j]);
        dp[j] = max(dp[j - 1], dp[j]);
        dp[j] = max(dp[j], max(cc[j - 1], 0) + A[i - 1] * B[j - 1]);
      }
    }
    return dp.back();
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
