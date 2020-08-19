#include <vector>
/*
 * @lc app=leetcode id=847 lang=cpp
 *
 * [847] Shortest Path Visiting All Nodes
 *
 * https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/
 *
 * algorithms
 * Hard (52.03%)
 * Total Accepted:    16.7K
 * Total Submissions: 32.2K
 * Testcase Example:  '[[1,2,3],[0],[0],[0]]'
 *
 * An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is
 * given as graph.
 *
 * graph.length = N, and j != i is in the list graph[i] exactly once, if and
 * only if nodes i and j are connected.
 *
 * Return the length of the shortest path that visits every node. You may start
 * and stop at any node, you may revisit nodes multiple times, and you may
 * reuse edges.
 *
 *
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [[1,2,3],[0],[0],[0]]
 * Output: 4
 * Explanation: One possible path is [1,0,2,0,3]
 *
 * Example 2:
 *
 *
 * Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
 * Output: 4
 * Explanation: One possible path is [0,1,4,2,3]
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= graph.length <= 12
 * 0 <= graph[i].length < graph.length
 *
 *
 */
class Solution {
public:
  int shortestPathLength(vector<vector<int>> &graph) {
    int N = graph.size();
    queue<pair<int, int>> q;
    for (int i = 0; i < N; i++)
      q.push(make_pair(i, 1 << i));
    int final_status = (1 << N) - 1;

    int steps = 0;
    int cc[(1 << N)][N];
    memset(cc, 0, sizeof(cc));
    // vector<unordered_set<int>> cc(N);

    while (!q.empty()) {
      int len = q.size();
      while (len-- > 0) {
        auto pair = q.front();
        q.pop();
        if (pair.second == final_status)
          return steps;
        for (auto suc : graph[pair.first]) {
          int next_status = pair.second | (1 << suc);
          if (next_status == final_status)
            return ++steps;
          if (cc[next_status][suc] == 0) {
            cc[next_status][suc] = 1;
            q.push(make_pair(suc, next_status));
          }
        }
      }
      steps++;
    }
    return INT_MAX;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
