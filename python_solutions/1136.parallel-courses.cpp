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
  int dfs(int i, vector<vector<int>> &relations, vector<int> &memo) {
    if (memo[i] > -1)
      return memo[i];
    if (memo[i] == -2) // Found a loop
      return 0x3f3f3f3f;
    memo[i] = -2;
    for (int s : relations[i])
      memo[i] = max(memo[i], 1 + dfs(s, relations, memo));
    if (memo[i] == -2)
      memo[i] = 0;
    return memo[i];
  }

  int minimumSemesters(int N, vector<vector<int>> &relations) {
    vector<vector<int>> g(N + 1, vector<int>());
    vector<int> memo(N + 1, -1);
    for (auto &r : relations)
      g[r[0]].push_back(r[1]);

    int res = -1;
    for (int i = 0; i < N; i++) {
      res = max(res, dfs(i, g, memo));
      if (res >= 0x3f3f3f3f)
        return -1;
    }
    return res + 1;
  }
};

int main() {
  Solution s;
  std::vector<vector<int>> relations = {{1, 3}, {2, 3}};
  relations = {{1, 2}, {2, 3}, {3, 1}};
  say(s.minimumSemesters(3, relations));
}