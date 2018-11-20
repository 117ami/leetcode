#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
/**

   Given a string s, find the longest palindromic subsequence's length in s. You
   may assume that the maximum length of s is 1000.
   Example 1:
   Input:
   "bbbab"
   Output:
   4
   One possible longest palindromic subsequence is "bbbb".
   Example 2:
   Input:
   "cbbd"
   Output:
   2
   One possible longest palindromic subsequence is "bb".

**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int longestPalindromeSubseq(string s) {
    string rs = s;
    reverse(rs.begin(), rs.end());
    vector<int> final(s.size() + 1), tmp(s.size() + 1);
    for (int i = 0; i < s.size(); i++) {
      for (int j = 0; j < s.size(); j++) {
        if (rs[j] == s[i])
          tmp[j + 1] = final[j] + 1;
        else
          tmp[j + 1] = max(tmp[j], final[j + 1]);
      }
      final = tmp;
    }
    for (auto i : final)
      cout << i << " ";
    cout << endl;
    return 0;
  }

  int dp(string s, int i, int j, vector<vector<int>> &cache) {
    if (cache[i][j] != 0)
      return cache[i][j];
    if (i > j)
      return 0;
    if (i == j)
      return 1;
    if (s[i] == s[j])
      cache[i][j] = 2 + dp(s, i + 1, j - 1, cache);
    else
      cache[i][j] = max(dp(s, i + 1, j, cache), dp(s, i, j - 1, cache));
    return cache[i][j];
  }
};

void random_string(char *s, int len) {
  static const char alphanum[] = "abcdefghijklmnopqrstuvwxyz";
  srand((unsigned)time(NULL));
  for (int i = 0; i < len; ++i) {
    s[i] = alphanum[rand() % (sizeof(alphanum) - 1)];
  }

  s[len] = 0;
}

int main() {
  Solution sol;
  string s{"hiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxrhiddqsc"
           "dxrhiddqscdxrhiddqscdxrhiddqscdxr"};
  s = "aabca";
  cout << s << ", " << s.size() << " : " << sol.longestPalindromeSubseq(s)
       << endl;
}
