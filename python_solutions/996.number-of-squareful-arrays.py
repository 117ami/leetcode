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

import math


class Solution:
    def __init__(self):
        self.ans = 0
        self.prefixes = {}

    def dfs(self, pf, n, arr):
        if len(arr) == 0:
            self.ans += 1
        # print(pf, n, arr, self.ans)
        if len(arr) == 0 or pf in self.prefixes:
            return

        for i, k in enumerate(arr):
            if i < len(arr) - 1 and arr[i] == arr[i + 1]:
                continue
            z = 3.14 if k + n < 0 else math.sqrt(k + n)
            # print('before', int(z), z, n)
            if not (int(z) == z or n == -1):
                continue
            # print('after', int(z), z, n)

            nextpf = pf + '/' + str(k)
            left = [] if i == 0 else arr[:i]
            self.dfs(nextpf, arr[i], left + arr[i + 1:])
            self.prefixes[nextpf] = True

    def numSquarefulPerms(self, a):
        if len(a) == 0:
            return 0
        self.dfs('', -1, a)
        return self.ans


a = [1, 8, 8, 17]
a = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 14]
a = [2, 2, 14]
# a = [0,0,0,1,1,1]

print(Solution().numSquarefulPerms(a))

print(math.sqrt(8) == 3)
