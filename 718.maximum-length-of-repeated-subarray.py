#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (47.47%)
# Total Accepted:    42.6K
# Total Submissions: 89.5K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
#
# Example 1:
#
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
#
#
#
#
# Note:
#
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#
#
#
#
#


class Solution:
    def findLength(self, a, b):
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if a[i] == b[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                    res = max(res, dp[i + 1][j + 1])
        return res


a = [1, 2, 3, 2, 1]
b = [3, 2, 1, 4, 7]
a, b = [1,0,0,0,1], [1,0,0,1,1]
s = Solution()
print(s.findLength(a, b))
