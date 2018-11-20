#include "aux.cpp"
/**
Given a list of words (without duplicates), please write a program that returns
all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at
least two shorter words in the given array.
Example:
Input:
["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat" can
be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.

 https://leetcode.com/problems/concatenated-words/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  unordered_set<string> visit;
  vector<string> findAllConcatenatedWordsInADict(vector<string> &words) {
    sort(words.begin(), words.end(),
         [](const string &a, const string &b) { return a.size() < b.size(); });
    vector<string> res;
    if (words.size() == 0)
      return res;
    for (auto s : words) {
      if (s.size() > 0 && concatenated(s))
        res.emplace_back(s);
      visit.insert(s);
    }
    return res;
  }

  bool concatenated(const string &s) {
    if (s.size() == 0 || visit.count(s))
      return true;
    for (int i = 1; i < s.size(); i++)
      // concatenate at least two non-empty string, that's why 1 <= i < s.size()
      if (visit.count(s.substr(0, i)) && concatenated(s.substr(i)))
        return true;
    return false;
  }
};

int main() {
  Solution s;
  std::vector<string> words = {"cats", "cat",         "catsdogcats",
                               "dog",  "dogcatsdog",  "hippopotamuses",
                               "rat",  "ratcatdogcat"};
  say(s.findAllConcatenatedWordsInADict(words));
}
