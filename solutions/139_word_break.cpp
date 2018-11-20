#include "aux.cpp"
/**
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated sequence
of one or more dictionary words.
Note:
        The same word in the dictionary may be reused multiple times in the
segmentation.
        You may assume the dictionary does not contain duplicate words.
Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen
apple".
            Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

 https://leetcode.com/problems/word-break/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  bool wordBreak(string s, vector<string> &wordDict) {
    unordered_map<string, bool> dict;
    return backtracking(s, wordDict, dict);
  }

  bool backtracking(string s, vector<string> &wordDict,
                    unordered_map<string, bool> &dict) {
    if (dict.find(s) != dict.end())
      return dict[s];
    for (auto w : wordDict) {
      if (s == w)
        return true;
      if (s.substr(0, w.size()) == w &&
          backtracking(s.substr(w.size()), wordDict, dict)) {
        dict[s] = true;
        return true;
      }
    }
    dict[s] = false;
    return false;
  }
};

int main() {
  Solution s;
  string ss = "catsandog";
  vector<string> wordDict = {"cats", "dog", "sand", "and", "cat", "og"};
  say(s.wordBreak(ss, wordDict));
}
