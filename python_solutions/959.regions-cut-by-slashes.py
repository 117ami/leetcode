#
# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#
# https://leetcode.com/problems/regions-cut-by-slashes/description/
#
# algorithms
# Medium (64.23%)
# Total Accepted:    11.7K
# Total Submissions: 18.2K
# Testcase Example:  '[" /","/ "]'
#
# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /,
# \, or blank space.  These characters divide the square into contiguous
# regions.
#
# (Note that backslash characters are escaped, so a \ is represented as "\\".)
#
# Return the number of regions.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input:
# [
# " /",
# "/ "
# ]
# Output: 2
# Explanation: The 2x2 grid is as follows:
#
#
#
#
# Example 2:
#
#
# Input:
# [
# " /",
# "  "
# ]
# Output: 1
# Explanation: The 2x2 grid is as follows:
#
#
#
#
# Example 3:
#
#
# Input:
# [
# "\\/",
# "/\\"
# ]
# Output: 4
# Explanation: (Recall that because \ characters are escaped, "\\/" refers to
# \/, and "/\\" refers to /\.)
# The 2x2 grid is as follows:
#
#
#
#
# Example 4:
#
#
# Input:
# [
# "/\\",
# "\\/"
# ]
# Output: 5
# Explanation: (Recall that because \ characters are escaped, "/\\" refers to
# /\, and "\\/" refers to \/.)
# The 2x2 grid is as follows:
#
#
#
#
# Example 5:
#
#
# Input:
# [
# "//",
# "/ "
# ]
# Output: 3
# Explanation: The 2x2 grid is as follows:
#
#
#
#
#
# Note:
#
#
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] is either '/', '\', or ' '.
#
#
#
#
#
#
#

# Reference : https://leetcode.com/problems/regions-cut-by-slashes/discuss/205739/Python-Union-Find-Solution-all-nodes'-parent-are-the-upper-left-corner

class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        p = [0 if i == 0 or j == 0 or i == n or j == n else i *
             (n + 1) + j for i in range(n + 1) for j in range(n + 1)]

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p1 = find(x)
            p2 = find(y)
            p[p1] = p2 
            return p1 == p2

        res = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    res += union(i * (n + 1) + j + 1, (i + 1) * (n + 1) + j)
                elif grid[i][j] == "\\":
                    res += union(i * (n + 1) + j, (i + 1) * (n + 1) + j + 1)
        return res


s = Solution()
grid = ["/\\", "\\/"]
# grid = ["///", "///", " / "]
print(s.regionsBySlashes(grid))
