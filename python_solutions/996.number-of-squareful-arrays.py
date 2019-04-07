#
# @lc app=leetcode id=996 lang=python3
#
# [996] Number of Squareful Arrays
#
# https://leetcode.com/problems/number-of-squareful-arrays/description/
#
# algorithms
# Hard (47.67%)
# Total Accepted:    4.3K
# Total Submissions: 8.9K
# Testcase Example:  '[1,17,8]'
#
# Given an array A of non-negative integers, the array is squareful if for
# every pair of adjacent elements, their sum is a perfect square.
#
# Return the number of permutations of A that are squareful.  Two permutations
# A1 and A2 differ if and only if there is some index i such that A1[i] !=
# A2[i].
#
#
#
# Example 1:
#
#
# Input: [1,17,8]
# Output: 2
# Explanation:
# [1,8,17] and [17,8,1] are the valid permutations.
#
#
# Example 2:
#
#
# Input: [2,2,2]
# Output: 1
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 12
# 0 <= A[i] <= 1e9
#
#

import collections
import math


class Solution:
    def numSquarefulPerms(self, a):
        if len(a) == 0:
            return 0
        c = collections.Counter(a)
        cand = {x: [y for y in c if int(
            math.sqrt(x + y)) ** 2 == x + y] for x in c}
        self.res = 0

        def dfs(x, cter):
            c[x] -= 1
            if cter == 0:
                self.res += 1
            [dfs(y, cter - 1) for y in cand[x] if c[y] > 0]
            c[x] += 1

        for x in c:
            dfs(x, len(a) - 1)

        return self.res


a = [1, 8, 8, 17]
# a = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 14]
# a = [2, 2, 14]
a = [0, 0, 0, 1, 1, 1]

print(Solution().numSquarefulPerms(a))
