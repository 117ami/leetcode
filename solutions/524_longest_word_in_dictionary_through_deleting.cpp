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

Given a string and a string dictionary, find the longest string in the
dictionary that can be formed by deleting some characters of the given string.
If there are more than one possible results, return the longest word with the
smallest lexicographical order. If there is no possible result, return the empty
string.
Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]
Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.

 https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  string findLongestWord(string s, vector<string> &d) {
    string res = "";
    for (string str : d)
      if (is_substring(s, str))
        res = str.size() > res.size()
                  ? str
                  : res.size() == str.size() && str < res ? str : res;

    return res;
  }
  bool is_substring(string s, string str) {
    int i = 0, j = 0;
    while (i < s.size() && j < str.size())
      if (s[i++] == str[j])
        j++;
    return j == str.size();
  }
};

int main() {
  Solution s;
  string ss = "abpcplea";
  std::vector<string> d = {"ale", "apple", "monkey", "plea"};
  say(s.findLongestWord(ss, d));
}
