/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (28.12%)
 * Total Accepted:    862.5K
 * Total Submissions: 3.1M
 * Testcase Example:  '"abcabcbb"'
 *
 * Given a string, find the length of the longest substring without repeating
 * characters.
 *
 *
 * Example 1:
 *
 *
 * Input: "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 *
 *
 * Example 2:
 *
 *
 * Input: "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 *
 *
 * Example 3:
 *
 *
 * Input: "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * ⁠            Note that the answer must be a substring, "pwke" is a
 * subsequence and not a substring.
 *
 *
 *
 *
 */

// #include "aux.cpp"

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int res = 0, leftmost = -1;
    unordered_map<int, int> charToIndex;
    for (int i = 0; i < s.length(); ++i) {
      int cur =
          charToIndex.find(s[i]) != charToIndex.end() ? charToIndex[s[i]] : -1;
      if (cur > leftmost)
        leftmost = cur;
      charToIndex[s[i]] = i;
      res = max(res, i - leftmost);
    }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// int main(int argc, char const *argv[]) {
//   Solution s;
//   string ss = "tmmzuxt";
//   say(s.lengthOfLongestSubstring(ss));
//   return 0;
// }
