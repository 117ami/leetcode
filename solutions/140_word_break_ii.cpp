#include "aux.cpp"
/**
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is a
valid dictionary word.Return all such possible sentences.
Note:
        The same word in the dictionary may be reused multiple times in the
segmentation.
        You may assume the dictionary does not contain duplicate words.
Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
 "cats and dog",
 "cat sand dog"
]
Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
 "pine apple pen apple",
 "pineapple pen apple",
 "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

 https://leetcode.com/problems/word-break-ii/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<string> wordBreak(string s, vector<string> &wordDict) {
    unordered_map<string, vector<string>> dict;
    return backtracking(s, wordDict, dict);
  }

  vector<string> backtracking(string s, vector<string> &wordDict,
                              unordered_map<string, vector<string>> &dict) {
    if (dict.find(s) != dict.end())
      return dict[s];
    for (auto w : wordDict) {
      if (s == w)
        dict[s].push_back(w);
      if (s.substr(0, w.size()) == w) {
        vector<string> tmp = backtracking(s.substr(w.size()), wordDict, dict);
        for (auto ss : tmp)
          dict[s].push_back(w + " " + ss);
      }
    }
    return dict[s];
  }
};

int main() {
  Solution s;
  string ss = "catsanddog";
  vector<string> wordDict = {"cats", "dog", "sand", "and", "cat", "og"};

  ss = "pineapplepenapple";
  wordDict = {"apple", "pen", "applepen", "pine", "pineapple"};

  ss = "aaaaaaa";
  wordDict = {"aaaa", "aa", "a"};
  say(s.wordBreak(ss, wordDict));
}
