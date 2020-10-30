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
  vector<string> expand(string S) {
    auto res = expand_unsorted(S);
    sort(res.begin(), res.end());
    return res;
  }
  vector<string> expand_unsorted(string S) {
    int open = (int)S.find_first_of('{');
    if (open == string::npos) return {S};
    int close = (int)S.find_first_of('}');
    string prefix = S.substr(0, open);
    std::vector<string> options = {""};
    for (int i = open + 1; i < close; i++) {
      char c = S[i];
      if (c == ',')
        options.push_back("");
      else
        options.back().push_back(c);
    }
    std::vector<string> suffixes = expand_unsorted(S.substr(close + 1));
    std::vector<string> res;
    for (auto &a : suffixes)
      for (auto &b : options) res.push_back(prefix + b + a);
    return res;
  }
};

int main() {
  Solution s;
  string expr = "{a,b}c{d,e}f";

  say(s.expand(expr));
}