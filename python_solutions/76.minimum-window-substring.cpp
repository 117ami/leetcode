#include <vector>
/*
 * @lc app=leetcode id=76 lang=cpp
 *
 * [76] Minimum Window Substring
 *
 * https://leetcode.com/problems/minimum-window-substring/description/
 *
 * algorithms
 * Hard (34.68%)
 * Total Accepted:    414.9K
 * Total Submissions: 1.2M
 * Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
 *
 * Given a string S and a string T, find the minimum window in S which will
 * contain all the characters in T in complexity O(n).
 *
 * Example:
 *
 *
 * Input: S = "ADOBECODEBANC", T = "ABC"
 * Output: "BANC"
 *
 *
 * Note:
 *
 *
 * If there is no such window in S that covers all characters in T, return the
 * empty string "".
 * If there is such window, you are guaranteed that there will always be only
 * one unique minimum window in S.
 *
 *
 */
class Solution {
public:
  string minWindow(string_view s, string_view t) {
    int cnt = t.size();
    int cc[128] = {0};
    for (auto c : t)
      cc[c]++;
    int start = 0, end = INT_MAX, left = 0;

    for (int i = 0; i < s.size(); i++) {
      if (cc[s[i]] > 0) cnt--;
      cc[s[i]]--;

      if (cnt == 0) {
        while (left < i && cc[s[left]] < 0) {
          cc[s[left]]++;
          left++;
        }
        if (i - left < end - start)
          start = left, end = i;
      }
    }
    return end < INT_MAX ? string(s.substr(start, end - start + 1)) : "";
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
