// Containers
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "conf.d/say.h"

using namespace std;
int dirs[5] = {-1, 0, 1, 0, -1};

// --------------------------------------------------------
class Solution {
public:
  vector<string> wordBreak(string s, vector<string> &wordDict) {
    std::unordered_map<string, vector<string>> dict;
    return backtracking(s, wordDict, dict);
  }

  vector<string> backtracking(string s, vector<string> &wordDict, unordered_map<string, vector<string>> &dict) {
    if (dict.find(s) != dict.end()) return dict[s];
    for (auto w : wordDict) {
      if (s == w) dict[s].push_back(w);
      if (s.substr(0, w.size()) == w) {
        std::vector<string> tmp = backtracking(s.substr(w.size()), wordDict, dict);
        for (auto ss : tmp) dict[s].push_back(w + " " + ss);
      }
    }
    return dict[s];
  }
};

int main() { Solution s; }