#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (36.45%)
# Total Accepted:    105.3K
# Total Submissions: 288.7K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
#
# Note:  
#
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
#
#


class Solution:
    def nthUglyNumber(self, n):
        arr = [1] * n
        u1, u2, u3 = 0, 0, 0
        for i in range(1, n):
            arr[i] = min(arr[u1] * 2, arr[u2] * 3, arr[u3] * 5)
            if arr[i] == arr[u1] * 2:
                u1 += 1
            if arr[i] == arr[u2] * 3:
                u2 += 1
            if arr[i] == arr[u3] * 5:
                u3 += 1
        return arr[-1]


s = Solution()
print(s.nthUglyNumber(10))
