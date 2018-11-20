#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <vector>
/**

   Given a string, your task is to count how many palindromic substrings in this
string.
   The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.
   Example 1:
   Input: "abc"
   Output: 3
   Explanation: Three palindromic strings: "a", "b", "c".
   Example 2:
   Input: "aaa"
   Output: 6
   Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
   Note:
   The input string length won't exceed 1000.

**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
  int cter = 0;

public:
  int countSubstrings(string s) {
    int size = s.size();
    if (size < 2)
      return size;
    for (int i = 0; i < size; i++) {
      span(s, i, i);
      span(s, i, i + 1);
    }
    return cter;
  };

private:
  void span(string s, int i, int j) {
    while (i >= 0 && j < s.size() && s[i] == s[j]) {
      i--;
      j++;
      cter++;
    }
  };
};

int main() {
  Solution sol;
  string s = "aaaa";
  cout << sol.countSubstrings(s) << endl;
}
