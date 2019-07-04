#include "aux.cpp"
/**
Given string S and adictionary of words words, find the number of words[i] that
is a subsequence of S. Example : Input: S = "abcde" words = ["a", "bb", "acd",
"ace"] Output: 3 Explanation: There are three words in words that are a
subsequence of S: "a", "acd", "ace". Note: All words in words and S will only
consists of lowercase letters. The length of S will be in the range of [1,
50000]. The length of words will be in the range of[1, 5000]. The length of
words[i] will be in the range of [1, 50].

 https://leetcode.com/problems/number-of-matching-subsequences/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int numMatchingSubseq(string s, vector<string> &words) {
    vector<pair<int, int>> pending[128];
    for (int i = 0; i < words.size(); i++)
      pending[words[i][0]].emplace_back(i, 1);

    for (char c : s) {
      auto nxt = pending[c];
      pending[c].clear();
      for (auto it : nxt)
        pending[words[it.first][it.second++]].push_back(it);
    }
    return pending[0].size();
  }
};

int main() {
  Solution s;
  string ss = "abcde";
  vector<string> words = {"a", "bb", "acd", "ace"};
  say(s.numMatchingSubseq(ss, words));
}
