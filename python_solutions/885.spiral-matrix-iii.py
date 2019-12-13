#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#
# https://leetcode.com/problems/spiral-matrix-iii/description/
#
# algorithms
# Medium (66.92%)
# Total Accepted:    14.2K
# Total Submissions: 21.2K
# Testcase Example:  '1\n4\n0\n0'
#
# On a 2 dimensional grid with R rows and C columns, we start at (r0, c0)
# facing east.
#
# Here, the north-west corner of the grid is at the first row and column, and
# the south-east corner of the grid is at the last row and column.
#
# Now, we walk in a clockwise spiral shape to visit every position in this
# grid. 
#
# Whenever we would move outside the boundary of the grid, we continue our walk
# outside the grid (but may return to the grid boundary later.) 
#
# Eventually, we reach all R * C spaces of the grid.
#
# Return a list of coordinates representing the positions of the grid in the
# order they were visited.
#
#
#
# Example 1:
#
#
# Input: R = 1, C = 4, r0 = 0, c0 = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
#
#
#
#
#
#
# Example 2:
#
#
# Input: R = 5, C = 6, r0 = 1, c0 = 4
# Output:
# [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#
#
#
#
#
#
#
#
# Note:
#
#
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C
#
#
#
#


class Solution:
    def spiralMatrixIII(self, r, c, r0, c0):
        # : int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        dx, dy, cter = 0, 1, 0
        while len(res) < r * c:
            for _ in range(cter // 2 + 1):
                if 0 <= r0 < r and 0 <= c0 < c:
                    res.append([r0, c0])
                r0, c0 = r0 + dx, c0 + dy
            dx, dy, cter = dy, -dx, cter + 1
        return res


s = Solution()
print(s.spiralMatrixIII(5, 6, 1, 4))
print(s.spiralMatrixIII(1, 4, 0, 0))

# li = [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[0,6],[1,6], [2,6], [3,6],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2]]
# for i in range(1, len(li)):
#     a = li[i]
#     b = li[i-1]
#     print(a[0]-b[0], a[1]-b[1])
