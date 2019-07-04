# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.

# @param {Integer[][]} obstacle_grid
# @return {Integer}
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ob = obstacleGrid
        m, n = len(ob), len(ob[0])
        if not m or ob[m-1][n-1] == 1: return 0

        for i in reversed(range(n)):
            if ob[m-1][i] == 0:
                ob[m-1][i] = 1
            else:
                for j in range(i + 1):
                    ob[m-1][j] = 0
                break

        for i in reversed(range(0, m - 1)): # xrange from 1
            if ob[i][n - 1] == 0:
                ob[i][n - 1] = 1
            else:
                for j in range(i + 1):
                    ob[j][n - 1] = 0
                break

        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                ob[i][j] = 0 if ob[i][j] == 1 else ob[i+1][j] + ob[i][j+1]

        return ob[0][0]

ob = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
s = Solution()
print (s.uniquePathsWithObstacles(ob))

