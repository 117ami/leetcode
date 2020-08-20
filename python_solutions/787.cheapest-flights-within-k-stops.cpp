#include <vector>
/*
 * @lc app=leetcode id=787 lang=cpp
 *
 * [787] Cheapest Flights Within K Stops
 *
 * https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
 *
 * algorithms
 * Medium (39.29%)
 * Total Accepted:    118.3K
 * Total Submissions: 301.1K
 * Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
 *
 * There are n cities connected by m flights. Each flight starts from city u
 * and arrives at v with a price w.
 *
 * Now given all the cities and flights, together with starting city src and
 * the destination dst, your task is to find the cheapest price from src to dst
 * with up to k stops. If there is no such route, output -1.
 *
 *
 * Example 1:
 * Input:
 * n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
 * src = 0, dst = 2, k = 1
 * Output: 200
 * Explanation:
 * The graph looks like this:
 *
 *
 * The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
 * marked red in the picture.
 *
 *
 * Example 2:
 * Input:
 * n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
 * src = 0, dst = 2, k = 0
 * Output: 500
 * Explanation:
 * The graph looks like this:
 *
 *
 * The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
 * marked blue in the picture.
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes n will be in range [1, 100], with nodes labeled from 0
 * to n - 1.
 * The size of flights will be in range [0, n * (n - 1) / 2].
 * The format of each flight will be (src, dst, price).
 * The price of each flight will be in the range [1, 10000].
 * k is in the range of [0, n - 1].
 * There will not be any duplicated flights or self cycles.
 *
 *
 */
#define pipii pair<int, pair<int, int>>
class Solution {
public:
  int bfs(int n, vector<vector<int>> &flights, int src, int dst, int K) {
    // int dp[n];
    // std::memset(dp, INT_MAX, sizeof(dp));
    int const MAX = std::numeric_limits<int>::max();
    std::vector<int> dp(n, MAX);
    dp[src] = 0;

    while (K-- >= 0) {
      bool updated = false;
      auto nextDP = dp;
      for (auto const &f : flights) {
        auto newCost = dp[f[0]] == MAX ? MAX : dp[f[0]] + f[2];
        if (newCost < nextDP[f[1]]) {
          updated = true;
          nextDP[f[1]] = newCost;
        }
      }

      if (!updated)
        break;

      dp = std::move(nextDP);
    }

    return dp[dst] == MAX ? -1 : dp[dst];
  }

  int findCheapestPrice(int n, vector<vector<int>> &graph, int src, int dst,
                        int K) {
    return bfs(n, graph, src, dst, K);
    // Each vector in graph contains 3 values: (srt, dst, weight)
    //   Return the smallest weight to reach each node from src
    vector<pair<int, int>> adj[n];
    for (auto &v : graph) {
      adj[v[0]].push_back(make_pair(v[1], v[2]));
    }

    priority_queue<pipii, vector<pipii>, greater<pipii>> pq;
    pq.push({0, {src, K + 1}});

    while (!pq.empty()) {
      auto top = pq.top();
      int p = top.first, u = top.second.first, steps = top.second.second;
      if (u == dst)
        return p;

      pq.pop();

      if (steps > 0)
        for (auto &pair : adj[u]) {
          int v = pair.first, weight = pair.second;
          pq.push({weight + p, {v, steps - 1}});
        }
    }
    return -1;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
