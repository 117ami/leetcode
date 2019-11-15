/*
 * @lc app=leetcode id=1254 lang=cpp
 *
 * [1254] Number of Closed Islands
 *
 * https://leetcode.com/problems/number-of-closed-islands/description/
 *
 * algorithms
 * Medium (59.94%)
 * Total Accepted:    5K
 * Total Submissions: 8.3K
 * Testcase Example:
 * '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
 *
 * Given a 2D grid consists of 0s (land) and 1s (water).  An island is a
 * maximal 4-directionally connected group of 0s and a closed island is an
 * island totally (all left, top, right, bottom) surrounded by 1s.
 *
 * Return the number of closed islands.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: grid =
 * [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
 * Output: 2
 * Explanation:
 * Islands in gray are closed because they are completely surrounded by water
 * (group of 1s).
 *
 * Example 2:
 *
 *
 *
 *
 * Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
 * Output: 1
 *
 *
 * Example 3:
 *
 *
 * Input: grid = [[1,1,1,1,1,1,1],
 * [1,0,0,0,0,0,1],
 * [1,0,1,1,1,0,1],
 * [1,0,1,0,1,0,1],
 * [1,0,1,1,1,0,1],
 * [1,0,0,0,0,0,1],
 * ⁠              [1,1,1,1,1,1,1]]
 * Output: 2
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= grid.length, grid[0].length <= 100
 * 0 <= grid[i][j] <=1
 *
 */
class Solution {
public:
  void infect(vector<vector<int>> &grid, int i, int j) {
    if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() ||
        grid[i][j] == 1)
      return;
      grid[i][j] = 1; 
    infect(grid, i + 1, j);
    infect(grid, i - 1, j);
    infect(grid, i, j + 1);
    infect(grid, i, j - 1);
  }
  int closedIsland(vector<vector<int>> &grid) {
    for (int i = 0; i < grid.size(); i++) {
      infect(grid, i, 0);
      infect(grid, i, grid[0].size() - 1);
    }
    for (int j = 0; j < grid.size(); j++) {
      infect(grid, 0, j);
      infect(grid, grid.size() - 1, j);
    }
    int res = 0;
    for (int i = 1; i < grid.size() - 1; i++)
      for (int j = 1; j < grid[0].size() - 1; j++) {
        if (grid[i][j] == 0) {
          res++;
          infect(grid, i, j);
        }
      }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
