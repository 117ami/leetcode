/*
 * @lc app=leetcode id=1048 lang=cpp
 *
 * [1048] Longest String Chain
 *
 * https://leetcode.com/problems/longest-string-chain/description/
 *
 * algorithms
 * Medium (44.33%)
 * Total Accepted:    4.3K
 * Total Submissions: 9.5K
 * Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
 *
 * Given a list of words, each word consists of English lowercase letters.
 *
 * Let's say word1 is a predecessor of word2 if and only if we can add exactly
 * one letter anywhere in word1 to make it equal to word2.  For example, "abc"
 * is a predecessor of "abac".
 *
 * A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
 * 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
 * word_3, and so on.
 *
 * Return the longest possible length of a word chain with words chosen from
 * the given list of words.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: ["a","b","ba","bca","bda","bdca"]
 * Output: 4
 * Explanation: one of the longest word chain is "a","ba","bda","bdca".
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= words.length <= 1000
 * 1 <= words[i].length <= 16
 * words[i] only consists of English lowercase letters.
 *
 *
 *
 *
 *
 */
class Solution {
public:
  int longestStrChain(vector<string> &words) {
    sort(words.begin(), words.end(),
         [](const string &a, const string &b) { return a.size() < b.size(); });
    unordered_map<string, int> res;
    int ans = 0;
    for (auto &w : words) {
      int maxlen = 1;
      for (int i = 0; i < w.size(); i++) {
        string left = i == 0 ? "" : w.substr(0, i),
               right = w.substr(i + 1, w.size() - i - 1);
        string substr = left + right;
        if (res.find(substr) != res.end())
          maxlen = max(res[substr] + 1, maxlen);
      }
      res[w] = maxlen;
      ans = max(maxlen, ans);
    }
    return ans;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
