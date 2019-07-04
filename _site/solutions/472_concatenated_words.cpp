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
  vector<string> findAllConcatenatedWordsInADict(vector<string> &words) {
    unordered_map<char, vector<string>> grouped;
    for (string w : words)
      if (w != "")
        grouped[w[0]].emplace_back(w);

    for (auto pair : grouped) {
    	std::vector<string> vs = pair.second;
      sort(
      	vs.begin(), vs.end(),
          [](const string &a, const string &b) { return a.size() < b.size(); });
      grouped[pair.first] = vs; 
      // say(pair.second);
    }

    unordered_map<string, int> visit;
    for (auto s : words)
      backtracking(s, words, visit, grouped);


    vector<string> res;
    for (auto const &s : words) {
      if (visit[s] > 1)
        res.emplace_back(s);
	}

    return res;
  }

  int backtracking(string s, std::vector<string> &words,
                   unordered_map<string, int> &visit,
                   unordered_map<char, std::vector<string>> &grouped) {
    if (visit.find(s) != visit.end())
      return visit[s];
    if (grouped.find(s[0]) != grouped.end()) {
      for (auto w : grouped[s[0]]) {
        if (w.length() > s.length())
          break;
        if (s == w) {
          visit[s] = max(visit[s], 1);
          return visit[s];
        } else if (s.substr(0, w.size()) == w &&
                   backtracking(s.substr(w.size()), words, visit, grouped) > 0) {
          visit[s] = 2;
          return 2;
        }
      }
    }
    visit[s] = 0;
    return 0;
  }
};

int main() {
  Solution s;
  std::vector<string> words = {"cats", "cat",         "catsdogcats", 
                               "dog",  "dogcatsdog",  "hippopotamuses",
                               "rat",  "ratcatdogcat"};
  say(s.findAllConcatenatedWordsInADict(words));
}
