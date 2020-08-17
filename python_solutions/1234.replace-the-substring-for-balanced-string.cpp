#include <vector>
/*
 * @lc app=leetcode id=1234 lang=cpp
 *
 * [1234] Replace the Substring for Balanced String
 *
 * https://leetcode.com/problems/replace-the-substring-for-balanced-string/description/
 *
 * algorithms
 * Medium (33.29%)
 * Total Accepted:    11.4K
 * Total Submissions: 34.1K
 * Testcase Example:  '"QWER"'
 *
 * You are given a string containing only 4 kinds of characters 'Q', 'W', 'E'
 * and 'R'.
 *
 * A string is said to be balanced if each of its characters appears n/4 times
 * where n is the length of the string.
 *
 * Return the minimum length of the substring that can be replaced with any
 * other string of the same length to make the original string s balanced.
 *
 * Return 0 if the string is already balanced.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "QWER"
 * Output: 0
 * Explanation: s is already balanced.
 *
 * Example 2:
 *
 *
 * Input: s = "QQWE"
 * Output: 1
 * Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is
 * balanced.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "QQQW"
 * Output: 2
 * Explanation: We can replace the first "QQ" to "ER".
 *
 *
 * Example 4:
 *
 *
 * Input: s = "QQQQ"
 * Output: 3
 * Explanation: We can replace the last 3 'Q' to make s = "QWER".
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s.length is a multiple of 4
 * s contains only 'Q', 'W', 'E' and 'R'.
 *
 *
 */
class Solution {
public:
  int balancedString(string s) {
    int cc[26] = {0};
    for (auto c : s)
      cc[c - 'A']++;
    // for (auto n: cc) say(n);
    int n = s.size(), cnt = 1 << 20, i = 0;
    for (int j = 0; j < n; j++) {
      char c = s[j];
      cc[c - 'A']--;
      while (i < n && cc['E' - 'A'] <= n / 4 && cc['Q' - 'A'] <= n / 4 &&
             cc['R' - 'A'] <= n / 4 && cc['W' - 'A'] <= n / 4) {
        cnt = min(cnt, j - i + 1);
        cc[s[i] - 'A']++, i++;
      }
    }
    return cnt;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
