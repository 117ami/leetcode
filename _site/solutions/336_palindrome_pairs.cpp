#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**

    Given a list of unique words, find all pairs of distinct indices (i, j) in
the given list, so that the concatenation of the two words, i.e. words[i] +
words[j] is a palindrome. Example 1: Given words = ["bat", "tab", "cat"] Return
[[0, 1], [1, 0]] The palindromes are ["battab", "tabbat"]

Example 2: Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
    The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
Credits:Special thanks to @dietpepsi for adding this problem and creating all
test cases.
 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<vector<int>> palindromePairs(vector<string> &words) {
    vector<vector<int>> res;
    if (words.size() < 2)
      return res;

    unordered_map<string, int> dict;
    for (size_t i = 0; i < words.size(); i++)
      dict[words[i]] = i;

    if (dict.find("") !=
        dict.end()) { // empty string " " concatenate with palindromes
      int idx = dict.find("")->second;
      for (int i = 0; i < words.size(); i++)
        if (i != idx && isPalindrome(words[i])) {
          res.push_back({i, idx});
          res.push_back({idx, i});
        }
    }

    for (int i = 0; i < words.size(); i++) {
      string xs = words[i];
      reverse(xs.begin(), xs.end());
      if (xs.size() > 0 && dict.find(xs) != dict.end()) {
        int xj = dict.find(xs)->second;
        if (xj != i)
          res.push_back({i, xj});
      }
    }

    for (int i = 0; i < words.size(); i++) {
      for (int j = 1; j < words[i].size(); j++) {
        string left = words[i].substr(0, j);
        string right = words[i].substr(j, words[i].size() - j);
        reverse(left.begin(), left.end());
        if (isPalindrome(right) && dict.find(left) != dict.end())
          res.push_back({i, dict.find(left)->second});

        reverse(left.begin(), left.end()); // reverse again back to normal
        reverse(right.begin(), right.end());
        if (isPalindrome(left) && dict.find(right) != dict.end())
          res.push_back({dict.find(right)->second, i});
      }
    }

    return res;
  }

  bool isPalindrome(string s) {
    int i = 0, j = s.size() - 1;
    while (i < j) {
      if (s[i++] != s[j--])
        return false;
    }
    return true;
  }
};

int main() {
  Solution s;
  vector<string> words = {"abcd", "dcba", "lls", "s", "sssll", ""};

  say(words.size());
  for (auto pair : s.palindromePairs(words)) {
    for (auto i : pair) {
      cout << i << " ";
    }
    cout << endl;
  }

}
