# https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations
# Hard (Difficulty)

# In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).
# In one move the snake can:
# Return the minimum number of moves to reach the target.
# If there is no way to reach the target, return -1.
#  
# Example 1:
#
# Example 2:
#  
# Constraints:
# Input: grid = [[0,0,0,0,0,1],
#                [1,1,0,0,1,0],
#                [0,0,0,0,1,1],
#                [0,0,1,0,1,0],
#                [0,1,1,0,0,0],
#                [0,1,1,0,0,0]]
# Output: 11
# Explanation:
# One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].
#
# Input: grid = [[0,0,1,1,1,1],
#                [0,0,0,0,1,1],
#                [1,1,0,0,0,1],
#                [1,1,1,0,0,1],
#                [1,1,1,0,0,1],
#                [1,1,1,0,0,0]]
# Output: 9
#
# xxxxxxxxxx
# class Solution {
# public:
#     int minimumMoves(vector<vector<int>>& grid) {
#         
#     }
# };


class Solution:
    def minimumMoves(self, grid):
        n = len(grid)
        cur = [(0, 0, 0)]  # tail_row, tail_col, horizontal or verticle
        memo = set(cur)
        res = 0

        while cur and (n - 1, n - 2, 0) not in cur:
            res += 1
            tmp = []
            for i, j, d in cur:
                if d == 0:  # horizontal
                    if j < n - 2 and grid[i][j + 2] == 0:
                        tmp.append((i, j + 1, d))
                    if i < n - 1 and grid[i +
                                          1][j] == 0 and grid[i + 1][j + 1] == 0:
                        tmp += [(i + 1, j, d), (i, j, 1)]
                else:  # verticle
                    if i < n - 2 and grid[i + 2][j] == 0:
                        tmp.append((i + 1, j, d))
                    if j < n - 1 and grid[i][j + \
                        1] == 0 and grid[i + 1][j + 1] == 0:
                        tmp += [(i, j, 0), (i, j + 1, d)]
            cur = set(tmp) - memo
            memo |= cur
        return res if cur else -1


grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0]]

print(Solution().minimumMoves(grid))
