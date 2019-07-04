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
    int t = 0, e = s.size() - 1;
    while (e >= 0) {
      if (s[t] == s[e])
        t++;
      e--;
    }
    if (t == s.size())
      return s;
    string com = s.substr(t, s.size() - t);
    reverse(com.begin(), com.end());
    return com + shortestPalindrome(s.substr(0, t)) + s.substr(t, s.size() - t);
  }
};
int main() {
  Solution s;
  string str = "abcd";
  say(s.shortestPalindrome(str));
}
