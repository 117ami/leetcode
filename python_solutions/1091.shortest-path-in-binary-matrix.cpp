/*
 * @lc app=leetcode id=1091 lang=cpp
 *
 * [1091] Shortest Path in Binary Matrix
 *
 * https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
 *
 * algorithms
 * Medium (32.11%)
 * Total Accepted:    2.4K
 * Total Submissions: 7.2K
 * Testcase Example:  '[[0,1],[1,0]]'
 *
 * In an N by N square grid, each cell is either empty (0) or blocked (1).
 *
 * A clear path from top-left to bottom-right has length k if and only if it is
 * composed of cells C_1, C_2, ..., C_k such that:
 *
 *
 * Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are
 * different and share an edge or corner)
 * C_1 is at location (0, 0) (ie. has value grid[0][0])
 * C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
 * If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] ==
 * 0).
 *
 *
 * Return the length of the shortest such clear path from top-left to
 * bottom-right.  If such a path does not exist, return -1.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [[0,1],[1,0]]
 * Output: 2
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [[0,0,0],[1,1,0],[1,1,0]]
 * Output: 4
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= grid.length == grid[0].length <= 100
 * grid[r][c] is 0 or 1
 *
 *
 */
using namespace std;
using pii = pair<int, int>;
using ll = long long;
using namespace std;
#define each(i, n) for (int i = 0; i <= int(n); ++i) // [0, n)
#define fori(n) for (int i = 0; i <= int(n); ++i)    // [0, n)
#include <cassert>
#define mp make_pair
#define dsize(v) (int)v.size()
template <class K, class V> bool exist(unordered_map<K, V> &m, K key) {
  return m.find(key) != m.end();
}
int direction[8][2] = {{-1, 0},  {1, 0},  {0, -1}, {0, 1},
                       {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

class Solution {
public:
  int shortestPathBinaryMatrix(vector<vector<int>> &g) {
    int n = dsize(g);
    if (g[0][0] == 1 || g[n - 1][n - 1] == 1)
      return -1;
    if (n == 1)
      return 1;
    queue<pii> q;
    q.push(mp(0, 0));
    g[0][0] = 1;
    while (!q.empty()) {
      auto p = q.front();
      q.pop();
      each(i, 7) {
        int x = direction[i][0] + p.first, y = direction[i][1] + p.second;
        if (x < 0 || x >= n || y < 0 || y >= n || g[x][y] != 0)
          continue;

        g[x][y] = g[p.first][p.second] + 1;
        q.push(mp(x, y));
        if (x == n - 1 && y == n - 1)
          return g[x][y];
      }
    }
    return -1;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
