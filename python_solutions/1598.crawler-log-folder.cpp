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
  int minOperations(vector<string> &logs) {
    int res = 0;
    for (auto &l : logs) {
      if (l.substr(0, 3) == "../")
        res = max(res - 1, 0);
      else if (l.substr(0, 2) != "./")
      res++;
    }
    return res;
  }
};

int main() { Solution s; }