/*
 * @lc app=leetcode id=940 lang=cpp
 *
 * [940] Distinct Subsequences II
 *
 * https://leetcode.com/problems/distinct-subsequences-ii/description/
 *
 * algorithms
 * Hard (41.38%)
 * Total Accepted:    9.7K
 * Total Submissions: 23.5K
 * Testcase Example:  '"abc"'
 *
 * Given a string S, count the number of distinct, non-empty subsequences of S
 * .
 *
 * Since the result may be large, return the answer modulo 10^9 + 7.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: "abc"
 * Output: 7
 * Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac",
 * "bc", and "abc".
 *
 *
 *
 * Example 2:
 *
 *
 * Input: "aba"
 * Output: 6
 * Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and
 * "aba".
 *
 *
 *
 * Example 3:
 *
 *
 * Input: "aaa"
 * Output: 3
 * Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
 *
 *
 *
 *
 *
 *
 *
 *
 * Note:
 *
 *
 * S contains only lowercase letters.
 * 1 <= S.length <= 2000
 *
 *
 *
 *
 *
 *
 *
 *
 *
 */
class Solution {
public:
  int distinctSubseqII(string S) {
    vector<long> e(26, 0); long mod = 1e9 + 7;
    for (auto c : S)
      e[c - 'a'] = accumulate(e.begin(), e.end(), 1L) % mod;
    return accumulate(e.begin(), e.end(), 0L) % mod;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
