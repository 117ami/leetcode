#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (49.73%)
# Total Accepted:    110.1K
# Total Submissions: 220.1K
# Testcase Example:  '3\n7'
#
#
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
#
# Note:
#
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#
#
# Example 2:
#
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
#
#
#

from itertools import combinations


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return [i for i in combinations(range(1, 10), k) if sum(i) == n]


# print(Solution().combinationSum3(3, 9))
