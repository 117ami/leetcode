/*
 * @lc app=leetcode id=97 lang=cpp
 *
 * [97] Interleaving String
 *
 * https://leetcode.com/problems/interleaving-string/description/
 *
 * algorithms
 * Hard (28.01%)
 * Total Accepted:    111.8K
 * Total Submissions: 398.7K
 * Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
 *
 * Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
 * s2.
 *
 * Example 1:
 *
 *
 * Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
 * Output: false
 *
 *
 */
#include "c.cpp"
using namespace std;
using VB = vector<bool>;
using VVB = vector<VB>;
// #define EACH(i, n) for (int i = 0; i <= int(n); ++i)
// #define EACHV(i, n) for (int i = int(n); i >= 0; --i)


class Solution {
public:
  bool isInterleave(string s1, string s2, string s3) {
    int m = s1.size(), n = s2.size(), p = s3.size();
    if (m + n != p)
      return false;
    VVB dp(m + 1, VB(n + 1, false));
    EACH(i, m) EACH(j, n) if (i == 0 && j == 0) dp[i][j] = true;
    else if (i == 0) dp[i][j] = dp[i][j - 1] && s2[j - 1] == s3[i + j - 1];
    else if (j == 0) dp[i][j] = dp[i - 1][j] && s1[i - 1] == s3[i + j - 1];
    else dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) ||
                    (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);

    return dp[m][n];
  }
};
