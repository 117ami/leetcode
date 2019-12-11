# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix
# Hard (Difficulty)

# Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbours of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighboors if they share one edge.
# Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.
# Binary matrix is a matrix with all cells equal to 0 or 1 only.
# Zero matrix is a matrix with all cells equal to 0.
#  
# Example 1:
# Example 2:
# Example 3:
# Example 4:
#  
# Constraints:
# Input: mat = [[0,0],[0,1]]
# Output: 3
# Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
#
# Input: mat = [[0]]
# Output: 0
# Explanation: Given matrix is a zero matrix. We don't need to change it.
#
# Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
# Output: 6
#
# Input: mat = [[1,0,0],[1,0,0]]
# Output: -1
# Explanation: Given matrix can't be a zero matrix
#
# xxxxxxxxxx
# class Solution {
# public:
#     int minFlips(vector<vector<int>>& mat) {
#         
#     }
# };

from functools import reduce


class Solution:
    def minFlips(self, mat):
        m, n = len(mat), len(mat[0])
        dirs = [0, 0, 1, 0, -1, 0]

        def getflip(i, j, bit):
            for d in range(5):
                x, y = i + dirs[d], j + dirs[d + 1]
                if m > x >= 0 <= y < n:
                    bit ^= (1 << (m * n - 1 - x * n - y))
            return bit

        b = reduce(lambda x, y: (x << 1) | y,
                   (i for row in mat for i in row))
        memo = set()
        queue = [(b, 0)]

        while queue:
            bit, d = queue.pop(0)
            if not bit:
                return d

            for i in range(m):
                for j in range(n):
                    nbit = getflip(i, j, bit)
                    if nbit not in memo:
                        memo.add(nbit)
                        queue.append((nbit, d + 1))
        return -1


mat = [[0, 0], [0, 1]]
mat = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
# mat = [[0]]
# mat = [[1, 0, 0], [1, 0, 0]]
# mat = [[1, 0], [1, 0]]
print(Solution().minFlips(mat))
