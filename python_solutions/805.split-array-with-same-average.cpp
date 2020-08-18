#include <vector>
/*
 * @lc app=leetcode id=805 lang=cpp
 *
 * [805] Split Array With Same Average
 *
 * https://leetcode.com/problems/split-array-with-same-average/description/
 *
 * algorithms
 * Hard (26.35%)
 * Total Accepted:    15.4K
 * Total Submissions: 58.5K
 * Testcase Example:  '[1,2,3,4,5,6,7,8]'
 *
 * In a given integer array A, we must move every element of A to either list B
 * or list C. (B and C initially start empty.)
 *
 * Return true if and only if after such a move, it is possible that the
 * average value of B is equal to the average value of C, and B and C are both
 * non-empty.
 *
 *
 * Example :
 * Input:
 * [1,2,3,4,5,6,7,8]
 * Output: true
 * Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both
 * of them have the average of 4.5.
 *
 *
 * Note:
 *
 *
 * The length of A will be in the range [1, 30].
 * A[i] will be in the range of [0, 10000].
 *
 *
 *
 *
 */
class Solution {
public:
  bool splitArraySameAverage(vector<int> &A) {
    if (A.size() <= 1)
      return false;

    int N = A.size(), S = std::accumulate(A.begin(), A.end(), 0);

    // Different with Python solution, dp[M] stores information on possible
    // lengths of lists whose sum is M. E.g., for A = {1, 3, 4, 5}, dp[4] = 6 =
    // 110 This 4 comes either from a list with length 1 (log 2) or length 2
    // (log 4). Another example, dp[9] = 12, means the sum of some list with
    // length 3 (or 2) is 9.
    int dp[S + 1];
    memset(dp, 0, sizeof dp);
    dp[0] = 1;

    for (auto a : A)
      for (int s = S - a; s >= 0; s--)
        dp[s + a] |= (dp[s] << 1);

    // for (auto zz : dp)
    //   say(zz);

    for (int len = 1; len < N; len++)
      if ((S * len) % N == 0 && ((1 << len) & dp[S * len / N]))
        return true;
    return false;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
