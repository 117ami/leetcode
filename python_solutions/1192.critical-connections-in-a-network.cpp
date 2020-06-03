/*
 * @lc app=leetcode id=1192 lang=cpp
 *
 * [1192] Critical Connections in a Network
 *
 * https://leetcode.com/problems/critical-connections-in-a-network/description/
 *
 * algorithms
 * Hard (48.72%)
 * Total Accepted:    50.4K
 * Total Submissions: 103.3K
 * Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
 *
 * There are n servers numbered from 0 to n-1 connected by undirected
 * server-to-server connections forming a network where connections[i] = [a, b]
 * represents a connection between servers a and b. Any server can reach any
 * other server directly or indirectly through the network.
 *
 * A critical connection is a connection that, if removed, will make some
 * server unable to reach some other server.
 *
 * Return all critical connections in the network in any order.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
 * Output: [[1,3]]
 * Explanation: [[3,1]] is also accepted.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 10^5
 * n-1 <= connections.length <= 10^5
 * connections[i][0] != connections[i][1]
 * There are no repeated connections.
 *
 *
 */
class Solution {
public:
  void dfs(int node, int par, int cur_lev, vector<int> &level, vector<int> &low,
           unordered_map<int, vector<int>> &g) {
    if (level[node] == INT_MAX) {
      level[node] = low[node] = cur_lev;
      for (auto neigh : g[node]) {
        if (level[neigh] == INT_MAX)
          dfs(neigh, node, cur_lev + 1, level, low, g);
      }
      int new_low = cur_lev;
      for (auto x : g[node])
        if (x != par)
          new_low = min(new_low, low[x]);
      low[node] = new_low;
    }
  }

  vector<vector<int>> criticalConnections(int n,
                                          vector<vector<int>> &connections) {
    unordered_map<int, vector<int>> g;
    for (auto &c : connections) {
      int a = c[0], b = c[1];
      g[a].push_back(b);
      g[b].push_back(a);
    }
    vector<int> level(n, INT_MAX);
    vector<int> low(n, __INT_MAX__);
    dfs(0, -1, 0, level, low, g);

    vector<vector<int>> res;
    for (auto &c : connections)
      if (low[c[0]] > level[c[1]] || low[c[1]] > level[c[0]])
        res.push_back(c);
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
