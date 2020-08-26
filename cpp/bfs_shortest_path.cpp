

int shortest_path(vector<vector<int>> &grid, int k) {
    // k stands for number of obstacles we can remove during BFS. 
    // For normal BFS to search for shortest path from left-top to right-bottom,
    // just set k = 0; 
    int m = grid.size(), n = grid[0].size();
    if (k >= m + n - 3)
      return m + n - 2;
    unordered_map<int, int> memo;
    memo[0] = 0;
    queue<pair<int, pair<int, int>>> q;
    q.push({0, {0, 0}});
    int steps = -1;

    while (!q.empty()) {
      steps++;
      size_t len = q.size();
      for (int i = 0; i < len; i++) {
        pair<int, pair<int, int>> x = q.front();
        q.pop();
        int obs = x.first, row = x.second.first, col = x.second.second;
        if (obs > k) continue;
        if (row == m - 1 && col == n - 1)
          return steps;
        for (int j = 0; j < 4; j++) {
          int r = row + dirs[j], c = col + dirs[j + 1];
          if (r >= 0 && r < m && c >= 0 && c < n) {
            int n_obs = grid[r][c] == 1 ? obs + 1 : obs;
            int key = 100 * r + c;
            if (memo.count(key) == 0 || n_obs < memo[key]) {
              memo[key] = n_obs;
              q.push({n_obs, {r, c}});
            }
          }
        }
      }
    }
    return -1;
  }