#include "aux.cpp"
/**
Given a string s, partition s such that every substring of the partition is a
palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
Example:
Input:"aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
cut.

 https://leetcode.com/problems/palindrome-partitioning-ii/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int minCut(string s) {
    int n = s.size();
    vector<int> cut(n + 1, 0);
    for (int i = 0; i <= n; i++)
      cut[i] = i - 1;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j <= i && i + j <= n && s[i - j] == s[i + j]; j++)
        cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j]);
      for (int j = 1; j <= i + 1 && i + j <= n && s[i - j + 1] == s[i + j]; j++)
        cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j + 1]);
    }
    return cut[n];
  }
};

int main() {
  Solution s;
  string ss = "kaabcbaap";
  ss = "kpp";
  say(s.minCut(ss));
}
