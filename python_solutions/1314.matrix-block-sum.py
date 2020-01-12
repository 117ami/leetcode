from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#
# https://leetcode.com/problems/matrix-block-sum/description/
#
# algorithms
# Medium (68.43%)
# Total Accepted:    2K
# Total Submissions: 3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# Given a m * n matrix mat and an integer K, return a matrix answer where each
# answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j
# - K <= c <= j + K, and (r, c) is a valid position in the matrix.
# 
# Example 1:
# 
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n, K <= 100
# 1 <= mat[i][j] <= 100
# 
#
class Solution:
    def matrixBlockSum(self, mat, k):
        m, n = len(mat), len(mat[0])
        x = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    x[i][j] = mat[0][0]
                elif i == 0:
                    x[i][j] = mat[0][j] + x[i][j-1]
                elif j == 0:
                    x[i][j] = mat[i][0] + x[i-1][j]
                else:
                    x[i][j] = x[i-1][j] + x[i][j-1] - x[i-1][j-1] + mat[i][j] 
        x = getPrefixSum(mat)
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rl, rr = max(0, i - k), min(m - 1, i + k)
                cl, cr = max(0, j - k), min(n - 1, j + k)
                if rl == 0 and cl == 0:
                    ans[i][j] = x[rr][cr]
                elif rl == 0:
                    ans[i][j] = x[rr][cr] - x[rr][cl-1]
                elif cl == 0:
                    ans[i][j] = x[rr][cr] - x[rl-1][cr]
                else:
                    ans[i][j] = x[rr][cr] + x[rl-1][cl-1] - x[rl-1][cr] - x[rr][cl-1]
        return ans 
        
sol = Solution()
mat, k = [[1,2,3],[4,5,6],[7,8,9]], 1
mat, k = [[1,2,3],[4,5,6],[7,8,9]], 2
print(sol.matrixBlockSum(mat, k))
