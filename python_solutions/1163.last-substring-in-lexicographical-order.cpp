#include <vector>
/*
 * @lc app=leetcode id=1163 lang=cpp
 *
 * [1163] Last Substring in Lexicographical Order
 *
 * https://leetcode.com/problems/last-substring-in-lexicographical-order/description/
 *
 * algorithms
 * Hard (34.10%)
 * Total Accepted:    14K
 * Total Submissions: 41K
 * Testcase Example:  '"abab"\r'
 *
 * Given a string s, return the last substring of s in lexicographical
 * order.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: "abab"
 * Output: "bab"
 * Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba",
 * "bab"]. The lexicographically maximum substring is "bab".
 *
 *
 * Example 2:
 *
 *
 * Input: "leetcode"
 * Output: "tcode"
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= s.length <= 4 * 10^5
 * s contains only lowercase English letters.
 *
 *
 */
class Solution {
public:
  string lastSubstring(string_view s) {
    int max = INT_MIN, j = -1;
    string_view r, ans = "";
    int dist = 0;

    // checking if all char in string are same.
    char cf = s[0];
    if (std::accumulate(
            s.begin(), s.end(), true,
            [&cf](bool pre, const char &c) { return pre && (c == cf); }))
      return string(s);

    for (int i = 0; i < s.size(); i++) {
      // traverse string , find largest char and compare
      // substring with result obtained so far
      if (max > s[i]) 
        continue;

      max = s[i];
      if (lexicographical_compare(s.begin() + i, s.end(), ans.begin(),
                                  ans.end()) == false)
        ans = s.substr(i, s.size());
    }
    return (string)ans;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
