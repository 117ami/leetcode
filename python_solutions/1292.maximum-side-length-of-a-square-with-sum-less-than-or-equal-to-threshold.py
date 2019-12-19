#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/
#
# algorithms
# Medium (40.52%)
# Total Accepted:    3.4K
# Total Submissions: 8.4K
# Testcase Example:  '[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]\r\n4\r'
#
# Given a m x n matrix mat and an integer threshold. Return the maximum
# side-length of a square with a sum less than or equal to threshold or return
# 0 if there is no such square.
#
#
# Example 1:
#
#
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as
# shown.
#
#
# Example 2:
#
#
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
# threshold = 1
# Output: 0
#
#
# Example 3:
#
#
# Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
# Output: 3
#
#
# Example 4:
#
#
# Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]],
# threshold = 40184
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 300
# m == mat.length
# n == mat[i].length
# 0 <= mat[i][j] <= 10000
# 0 <= threshold <= 10^5
#
#
#


class Solution:
    def lessEqual(self, k, prefix_sum, t):
        m, n = len(prefix_sum) - 1, len(prefix_sum[0]) - 1
        res = 0
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                res = prefix_sum[i + k][j + k] + prefix_sum[i][j] - \
                    prefix_sum[i + k][j] - prefix_sum[i][j + k]
                if res <= t:
                    return True
        return False

    def maxSideLength(self, mat, t):
        m, n = len(mat), len(mat[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - \
                    1] - prefix_sum[i - 1][j - 1] + mat[i - 1][j - 1]

        lo, hi = 0, min(m, n)
        while lo <= hi:
            mi = (lo + hi) // 2
            if self.lessEqual(mi, prefix_sum, t):
                lo = mi + 1
            else:
                hi = mi - 1
            # print(lo, hi)
        # return hi
        return 1 + hi if self.lessEqual(1 + hi, prefix_sum, t) else hi
