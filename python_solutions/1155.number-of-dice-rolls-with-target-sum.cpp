#include <vector>
/*
 * @lc app=leetcode id=1155 lang=cpp
 *
 * [1155] Number of Dice Rolls With Target Sum
 *
 * https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
 *
 * algorithms
 * Medium (48.89%)
 * Total Accepted:    44K
 * Total Submissions: 90.1K
 * Testcase Example:  '1\n6\n3'
 *
 * You have d dice, and each die has f faces numbered 1, 2, ..., f.
 *
 * Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7
 * to roll the dice so the sum of the face up numbers equals target.
 *
 *
 * Example 1:
 *
 *
 * Input: d = 1, f = 6, target = 3
 * Output: 1
 * Explanation:
 * You throw one die with 6 faces.  There is only one way to get a sum of 3.
 *
 *
 * Example 2:
 *
 *
 * Input: d = 2, f = 6, target = 7
 * Output: 6
 * Explanation:
 * You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
 * 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
 *
 *
 * Example 3:
 *
 *
 * Input: d = 2, f = 5, target = 10
 * Output: 1
 * Explanation:
 * You throw two dice, each with 5 faces.  There is only one way to get a sum
 * of 10: 5+5.
 *
 *
 * Example 4:
 *
 *
 * Input: d = 1, f = 2, target = 3
 * Output: 0
 * Explanation:
 * You throw one die with 2 faces.  There is no way to get a sum of 3.
 *
 *
 * Example 5:
 *
 *
 * Input: d = 30, f = 30, target = 500
 * Output: 222616187
 * Explanation:
 * The answer must be returned modulo 10^9 + 7.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= d, f <= 30
 * 1 <= target <= 1000
 *
 */
int MOD = 1000000007;
class Solution {
public:
  int numRollsToTarget(int d, int f, int target) {
    if (d * f < target)
      return 0;
    if (d * f == target)
      return 1;
    long dp[d + 1][target + 1];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;

    for (int i = 1; i <= d; i++)
      for (int j = 1; j <= target; j++) {
        long n = 0;
        if (i == 1)
          dp[i][j] = int(j > 0 && j <= f);
        else {
          for (int k = 1; k <= min(f, j); k++)
            n = (n + dp[i - 1][j - k]) % MOD;
        }
        dp[i][j] += n;
      }
    return dp[d][target];
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
