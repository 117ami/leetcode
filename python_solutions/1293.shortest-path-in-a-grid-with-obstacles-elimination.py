#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
#
# algorithms
# Hard (39.49%)
# Total Accepted:    3.1K
# Total Submissions: 7.9K
# Testcase Example:  '[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1'
#
# Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In
# one step, you can move up, down, left or right from and to an empty cell.
# 
# Return the minimum number of steps to walk from the upper left corner (0, 0)
# to the lower right corner (m-1, n-1) given that you can eliminate at most k
# obstacles. If it is not possible to find such walk return -1.
# 
# 
# Example 1:
# 
# 
# Input: 
# grid = 
# [[0,0,0],
# [1,1,0],
# ⁠[0,0,0],
# [0,1,1],
# ⁠[0,0,0]], 
# k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10. 
# The shortest path with one obstacle elimination at position (3,2) is 6. Such
# path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# grid = 
# [[0,1,1],
# [1,1,1],
# [1,0,0]], 
# k = 1
# Output: -1
# Explanation: 
# We need to eliminate at least two obstacles to find such a walk.
# 
# 
# 
# Constraints:
# 
# 
# grid.length == m
# grid[0].length == n
# 1 <= m, n <= 40
# 1 <= k <= m*n
# grid[i][j] == 0 or 1
# grid[0][0] == grid[m-1][n-1] == 0
# 
#
class Solution:
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])
        if k >= m + n - 3: return m + n - 2 
        
        memo = {(0, 0): 0}
        q = [(0, 0, 0)] # row, col, number of obstacles 
        steps = 0

        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                row, col, obs = q.pop(0)
                if obs > k: continue 
                if row == m - 1 and col == n - 1:
                    return steps 
                dirs = [0, 1, 0, -1, 0]
                for i in range(4):
                    r, c = row + dirs[i], col + dirs[i+1]
                    if 0 <= r < m and 0 <= c < n:
                        n_obs = obs + 1 if grid[r][c] == 1 else obs 
                        if n_obs < memo.get((r, c), 1600):
                            memo[(r, c)] = n_obs
                            q.append((r, c, n_obs))
            steps += 1
        return -1 
                    
grid = [[0,0,0], [2,1,1], [0,0,0], [0,1,1], [0,0,0]]
k = 1       
s = Solution()
print(s.shortestPath(grid, k))


