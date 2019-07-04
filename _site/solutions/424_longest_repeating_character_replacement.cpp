#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given a string that consists of only uppercase English letters, you can replace
any letter in the string with another letter at most k times. Find the length of
a longest substring containing all repeating letters you can get after
performing the above operations.
Note:
Both the string's length and k will not exceed 104.
Example 1:
Input:
s = "ABAB", k = 2
Output:
4
Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:
Input:
s = "AABABBA", k = 1
Output:
4
Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int characterReplacement(string s, int k) {
    int res = 0, start = 0, max_count = 0;
    vector<int> counts(26, 0);
    for (int i = 0; i < s.size(); i++) {
      max_count = max(max_count, ++counts[s[i] - 'A']);
      while (i - start + 1 - max_count > k) {
        counts[s[start] - 'A']--;
        start++;
      }
      res = max(res, i - start + 1);
    }
    return res;
  }
};

int main() {
  Solution s;
  string str = "ABCDEFGAB";
  int k = 2;
  k = s.characterReplacement(str, k);
  say(k);
}
