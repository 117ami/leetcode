#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.09%)
# Total Accepted:    142.5K
# Total Submissions: 383.5K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
#
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
# Example 2:
#
#
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
# Note: Your solution should be in logarithmic time complexity.
#
#

import math


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([n // (5**j) for j in range(1, int(math.log(n, 5)) + 1)]) if n > 0 else 0


# print(Solution().trailingZeroes(24))
