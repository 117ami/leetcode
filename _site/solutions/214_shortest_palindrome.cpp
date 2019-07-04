#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given a string s, you are allowed to convert it to a palindrome by adding
characters in front of it. Find and return the shortest palindrome you can find
by performing this transformation.
Example 1:
Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:
Input: "abcd"
Output: "dcbabcd"

 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  string shortestPalindrome(string s) {
    string rev_s = s;
    reverse(rev_s.begin(), rev_s.end());
    string xp = s + "#" + rev_s;

    vector<int> pmt(xp.size(), -1);
    int i = 0, j = -1, psz = xp.size();
    while (i < psz) {
      if (j == -1 || xp[i] == xp[j]) {
        i++;
        j++;
        pmt[i] = j;
      } else
        j = pmt[j];
    }
    i = pmt.back();
    xp = s.substr(i + 1, s.size() - i);
    reverse(xp.begin(), xp.end());
    return xp + s;
  }
};
int main() {
  Solution s;
  string str = "aacecaaa";
  say(s.shortestPalindrome(str));
}
