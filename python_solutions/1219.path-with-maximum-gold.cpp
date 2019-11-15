/*
 * @lc app=leetcode id=1219 lang=cpp
 *
 * [1219] Path with Maximum Gold
 *
 * https://leetcode.com/problems/path-with-maximum-gold/description/
 *
 * algorithms
 * Medium (61.31%)
 * Total Accepted:    9K
 * Total Submissions: 14.6K
 * Testcase Example:  '[[0,6,0],[5,8,7],[0,9,0]]'
 *
 * In a gold mine grid of size m * n, each cell in this mine has an integer
 * representing the amount of gold in that cell, 0 if it is empty.
 *
 * Return the maximum amount of gold you can collect under the
 * conditions:
 *
 *
 * Every time you are located in a cell you will collect all the gold in that
 * cell.
 * From your position you can walk one step to the left, right, up or down.
 * You can't visit the same cell more than once.
 * Never visit a cell with 0 gold.
 * You can start and stop collecting gold from any position in the grid that
 * has some gold.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
 * Output: 24
 * Explanation:
 * [[0,6,0],
 * ⁠[5,8,7],
 * ⁠[0,9,0]]
 * Path to get the maximum gold, 9 -> 8 -> 7.
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
 * Output: 28
 * Explanation:
 * [[1,0,7],
 * ⁠[2,0,6],
 * ⁠[3,4,5],
 * ⁠[0,3,0],
 * ⁠[9,0,20]]
 * Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= grid.length, grid[i].length <= 15
 * 0 <= grid[i][j] <= 100
 * There are at most 25 cells containing gold.
 *
 */
class Solution {
public:
  int dfs(vector<vector<int>> &grid, int i, int j) {
    if (grid[i][j] == 0)
      return 0;
    int result = 0;
    int temp = grid[i][j];
    grid[i][j] = 0;
    if (i > 0)
      result = max(result, temp + dfs(grid, i - 1, j));
    if (j > 0)
      result = max(result, temp + dfs(grid, i, j - 1));
    if (i < grid.size() - 1)
      result = max(result, temp + dfs(grid, i + 1, j));
    if (j < grid[0].size() - 1)
      result = max(result, temp + dfs(grid, i, j + 1));
    grid[i][j] = temp;
    return result;
  }
  int getMaximumGold(vector<vector<int>> &grid) {
    int result = 0;
    for (int i = 0; i < grid.size(); i++)
      for (int j = 0; j < grid[0].size(); j++)
        result = max(result, dfs(grid, i, j));
    return result;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
