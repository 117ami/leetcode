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

// --------------------------------------------------------
class Solution {
public:
  int dp[70][70][70];
  int dirs[10] = {-1, -1, 0, -1, 1, 0, 0, 1, 1, -1};
  
  int dfs(int R, int C, int r, int c1, int c2, vector<vector<int>> &grid) {
    if (r == R) return 0;
    int &ans = dp[r][c1][c2];
    if (ans > -1) return ans;

    for (int i = 0; i < 9; i++) {
      int nc1 = c1 + dirs[i], nc2 = c2 + dirs[i + 1];
      if (nc1 >= 0 && nc1 <= C - 1 && nc2 >= 0 && nc2 <= C - 1 && nc2 > nc1)
        ans = max(ans, dfs(R, C, r + 1, nc1, nc2, grid));
    }
    ans += grid[r][c1] + grid[r][c2];
    return ans;
  }

  int cherryPickup(vector<vector<int>> &grid) {
    int res = 0;
    int R = grid.size(), C = grid[0].size();
    memset(dp, -1, sizeof(dp));
    return dfs(R, C, 0, 0, C - 1, grid);
  }
};

int main() {
  Solution s;
  vector<vector<int>> grid = {{1, 0, 0, 0, 0, 0, 1},
                              {2, 0, 0, 0, 0, 3, 0},
                              {2, 0, 9, 0, 0, 0, 0},
                              {0, 3, 0, 5, 4, 0, 0},
                              {1, 0, 2, 3, 0, 0, 6}};
  grid = {{8, 8, 10, 9, 1, 7}, {8, 8, 1, 8, 4, 7}, {8, 6, 10, 3, 7, 7}, {3, 0, 9, 3, 2, 7}, {6, 8, 9, 4, 2, 5},
          {1, 1, 5, 8, 8, 1},  {5, 6, 5, 2, 9, 9}, {4, 4, 6, 2, 5, 4},  {4, 4, 5, 3, 1, 6}, {9, 2, 2, 1, 9, 3}};

  say(s.cherryPickup(grid));
}