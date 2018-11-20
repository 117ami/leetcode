#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>
/**
Given a list of strings words representing an English Dictionary, find the
longest word in words that can be built one character at a time by other words
in words.  If there is more than one possible answer, return the longest word
with the smallest lexicographical order.  If there is no answer, return the
empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and
"worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary.
However, "apple" is lexicographically smaller than "apply".
Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].

 https://leetcode.com/problems/longest-word-in-dictionary/description/
 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  string longestWord(vector<string> &words) {
    string res = "";
    sort(words.begin(), words.end());
    unordered_set<string> us;
    for (auto w : words) {
      if (1 == w.size() || us.count(w.substr(0, w.size() - 1))) {
        res = w.size() > res.size() ? w : res;
        us.insert(w);
      }
    }
    return res;
  }
};

int main() {
  Solution s;
  vector<string> words = {"m",   "mo",   "moc",   "moch", "mocha", "l",  "la",
                          "lat", "latt", "latte", "c",    "ca",    "cat"};
  words = {"yo",  "ew",   "fc", "zrc", "yodn", "fcm",  "qm",
           "qmo", "fcmz", "z",  "ewq", "yod",  "ewqz", "y"};
  //           words = {"w", "wo", "wor", "worl", "world"};
  say(s.longestWord(words));
}
