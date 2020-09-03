from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import heapq 
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007
#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
# https://leetcode.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (62.60%)
# Total Accepted:    53.7K
# Total Submissions: 85.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square array of integers A, we want the minimum sum of a falling path
# through A.
# 
# A falling path starts at any element in the first row, and chooses one
# element from each row.  The next row's choice must be in a column that is
# different from the previous row's column by at most one.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: 12
# Explanation: 
# The possible falling paths are:
# 
# 
# 
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# 
# 
# The falling path with the smallest sum is [1,4,7], so the answer is 12.
# 
# 
# Constraints:
# 
# 
# 1 <= A.length == A[0].length <= 100
# -100 <= A[i][j] <= 100
# 
# 
#
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        M = 10001
        dp = [[M] * 101 for _ in range(101)]
        def solve(i, j, ns):
            sz = len(ns)
            if i >= sz or j >= sz or j < 0: return M 
            if i == sz - 1: return ns[i][j]
            if dp[i][j] < M: return dp[i][j]
            ans = min(solve(i + 1, j, ns), solve(i + 1, j - 1, ns), solve(i + 1, j + 1, ns)) + ns[i][j]
            dp[i][j] = ans 
            return ans 

        return min(map(lambda j: solve(0, j, A), range(len(A))))

        

sol = Solution()


ns = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.minFallingPathSum(ns))
