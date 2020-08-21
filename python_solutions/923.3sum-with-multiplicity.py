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
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#
# https://leetcode.com/problems/3sum-with-multiplicity/description/
#
# algorithms
# Medium (35.39%)
# Total Accepted:    17.6K
# Total Submissions: 49.6K
# Testcase Example:  '[1,1,2,2,3,3,4,4,5,5]\n8'
#
# Given an integer array A, and an integer target, return the number of tuples
# i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
#
# As the answer can be very large, return it modulo 10^9 + 7.
#
#
#
# Example 1:
#
#
# Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation:
# Enumerating by the values (A[i], A[j], A[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
#
#
#
# Example 2:
#
#
# Input: A = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation:
# A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
#
#
#
#
#
# Note:
#
#
# 3 <= A.length <= 3000
# 0 <= A[i] <= 100
# 0 <= target <= 300
#
#


class Solution:
    def threeSumMulti(self, nums, t):
        cnt = [0] * 301
        for n in nums:
            cnt[n] += 1
        nums = sorted(list(set(nums)))
        ans = 0
        # print(nums, cnt)
        for i, ni in enumerate(nums):
            for j, nj in enumerate(nums[i:]):
                if ni + nj > t: break
                diff = t - ni - nj
                if diff < nj or cnt[diff] == 0:
                    continue
                if j == 0:
                    if diff == ni:
                        ans += cnt[ni] * (cnt[ni] - 1) * (cnt[ni] - 2) // 6
                    else:
                        ans += cnt[ni] * (cnt[ni] - 1) * cnt[diff] // 2
                else:
                    if diff == ni:
                        ans += cnt[ni] * (cnt[ni] - 1) * cnt[nj] // 2
                    elif diff == nj:
                        ans += cnt[ni] * cnt[nj] * (cnt[nj] - 1) // 2
                    else:
                        ans += cnt[ni] * cnt[nj] * cnt[diff]
                # print(ni, nj, diff, ans)
                ans %= 10**9 + 7
        return ans


sol = Solution()
# nums, t = [1,1,2,2,2,2], 5
nums, t = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8
print(sol.threeSumMulti(nums, t))
