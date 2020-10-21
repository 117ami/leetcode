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
  int wordsTyping(vector<string> &sentence, int rows, int cols) {
    int cnt = 0, n = sentence.size();
    std::unordered_map<int, int> cc;
    for (int i = 0; i < rows; i++) {
      int start = cnt % n;
      if (cc.count(start) == 0) {
        int j = 0, k = start, c = 0;
        while (j + sentence[k].size() <= cols) {
          c += 1;
          j += sentence[k].size() + 1;
          k = (k + 1) % n;
        }
        cnt += c;
        cc.emplace(start, c);
      } else
        cnt += cc[start];
    }

    return cnt / n;
  }
};

int main() {
  Solution s;
  vector<string> ss = {"a", "bcd", "e"};
  ss = {"pwievhoi",   "nngx",   "bbfnxbtx",   "qvfpise",  "xjzue",
        "ascrcacnmo", "bknodn", "spvlvcktbw", "rhklcmpd", "lwjxnfhx"};
  int r = 9593, c = 3340;
  say(s.wordsTyping(ss, r, c));
}