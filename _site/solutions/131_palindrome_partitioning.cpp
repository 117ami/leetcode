#include "aux.cpp"
/**
Given a string s, partition s such that every substring of the partition is a
palindrome.
Return all possible palindrome partitioning of s.
Example:
Input:"aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

 https://leetcode.com/problems/palindrome-partitioning/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<vector<string>> partition(string s) {
    vector<vector<string>> res;
    if (s.length() == 0)
      return res;
    if (s.length() == 1)
      return {{s}};
    for (int i = 1; i <= s.length(); i++) {
      if (!ispol(s.substr(0, i)))
        continue;
      for (auto rest : partition(s.substr(i))) {
        vector<string> vs = {s.substr(0, i)};
        vs.insert(vs.end(), rest.begin(), rest.end());
        res.push_back(vs);
      }
      if (i == s.length())
        res.push_back({s});
    }
    return res;
  }

  bool ispol(string s) {
    if (s.length() <= 1)
      return true;
    for (int i = 0; i < s.length() / 2; i++)
      if (s[i] != s[s.length() - i - 1])
        return false;
    return true;
  }
};

int main() {
  Solution s;
  string ss = "bb";
  for (auto xxx : s.partition(ss))
    say(xxx);
}
