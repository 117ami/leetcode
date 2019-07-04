/*
 * @lc app=leetcode id=1092 lang=cpp
 *
 * [1092] Shortest Common Supersequence
 *
 * https://leetcode.com/problems/shortest-common-supersequence/description/
 *
 * algorithms
 * Hard (43.85%)
 * Total Accepted:    1.4K
 * Total Submissions: 3.2K
 * Testcase Example:  '"abac"\n"cab"'
 *
 * Given two strings str1 and str2, return the shortest string that has both
 * str1 and str2 as subsequences.  If multiple answers exist, you may return
 * any of them.
 *
 * (A string S is a subsequence of string T if deleting some number of
 * characters from T (possibly 0, and the characters are chosen anywhere from
 * T) results in the string S.)
 *
 *
 *
 * Example 1:
 *
 *
 * Input: str1 = "abac", str2 = "cab"
 * Output: "cabac"
 * Explanation:
 * str1 = "abac" is a substring of "cabac" because we can delete the first "c".
 * str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
 * The answer provided is the shortest such string that satisfies these
 * properties.
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= str1.length, str2.length <= 1000
 * str1 and str2 consist of lowercase English letters.
 *
 */
class Solution {
public:
  string shortestCommonSupersequence(string s, string t) {
    int m = s.size(), n = t.size(), L[m + 1][n + 1];
    for (int i = 0; i <= m; i++)
      for (int j = 0; j <= n; j++)
        if (i == 0 || j == 0)
          L[i][j] = 0;
        else if (s[i - 1] == t[j - 1])
          L[i][j] = L[i - 1][j - 1] + 1;
        else
          L[i][j] = max(L[i - 1][j], L[i][j - 1]);

    string res(m + n - L[m][n], '#');
    int i = m, j = n, index = m + n - L[m][n];

    while (i > 0 && j > 0) {
      if (s[i - 1] == t[j - 1])
        res[--index] = s[--i], j--;
      else if (L[i - 1][j] > L[i][j - 1])
        res[--index] = s[--i]; 
      else
        res[--index] = t[--j];
    }

    if (i + j == 0) return res;
    else if (j > 0) while (j > 0) res[--index] = t[--j];
    else while (i > 0) res[--index] = s[--i];
    return res; 
  }
};	

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
