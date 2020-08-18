#include <vector>
/*
 * @lc app=leetcode id=30 lang=cpp
 *
 * [30] Substring with Concatenation of All Words
 *
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
 *
 * algorithms
 * Hard (25.41%)
 * Total Accepted:    180.6K
 * Total Submissions: 710.9K
 * Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
 *
 * You are given a string, s, and a list of words, words, that are all of the
 * same length. Find all starting indices of substring(s) in s that is a
 * concatenation of each word in words exactly once and without any intervening
 * characters.
 *
 *
 *
 * Example 1:
 *
 *
 * Input:
 * ⁠ s = "barfoothefoobarman",
 * ⁠ words = ["foo","bar"]
 * Output: [0,9]
 * Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
 * respectively.
 * The output order does not matter, returning [9,0] is fine too.
 *
 *
 * Example 2:
 *
 *
 * Input:
 * ⁠ s = "wordgoodgoodgoodbestword",
 * ⁠ words = ["word","good","best","word"]
 * Output: []
 *
 *
 */
class Solution {
public:
  vector<int> findSubstring(string s, vector<string> &words) {
    if (s.empty() || words.empty())
      return {};

    size_t _hash = std::accumulate(words.begin(), words.end(), (size_t)0, [](size_t a, string &w) {
      return a + std::hash<string_view>{}(std::string_view(w));
    });

    int n = s.size(), num = words.size(), len = words[0].size();
    std::vector<int> indexes;

    for (int i = 0; i < len ; i++) {
      size_t local_hash = 0, cnt = 0;
      for (int j = i; j + len <= n; j += len) {
        local_hash += std::hash<std::string_view>{}(std::string_view(&s[j], len));
        cnt++;

        if (cnt < num) continue;

        // remove left word's hash value 
        if (cnt > num)
          local_hash -= std::hash<std::string_view>{}( std::string_view(&s[j - num * len], len));

        if (local_hash == _hash) indexes.push_back(j - num * len + len);
        say(indexes);say(vector<int>{i, j});
      }
    }
    return indexes;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
