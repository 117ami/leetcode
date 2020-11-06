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
  string addBoldTag(string s, vector<string> &dict) {
    vector<int> bold(s.length(), false);
    for (auto &w : dict) {
      auto start = s.find(w);
      while (start != string::npos) {
        for (int i = start; i < start + w.length(); i++) bold[i] = true;
        start = s.find(w, start + 1);
      }
    }
    string res = "";
    int i = 0, n = s.length();
    while (i < n) {
      if (bold[i] == false)
        res.push_back(s[i++]);
      else {
        res += "<b>";
        while (i < n && bold[i] == true) res.push_back(s[i++]);
        res += "</b>";
      }
    }
    return res;
  }
};

int main() {
  Solution s;
  string t = "aaabbcc";
  vector<string> dict = {"aaa", "aab", "bc"};
  say(s.addBoldTag(t, dict));
}