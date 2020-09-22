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
# @lc app=leetcode id=1589 lang=python3
#
# [1589] Maximum Sum Obtained of Any Permutation
#
# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/
#
# algorithms
# Medium (30.00%)
# Total Accepted:    3.8K
# Total Submissions: 11.5K
# Testcase Example:  '[1,2,3,4,5]\n[[1,3],[0,1]]'
#
# We have an array of integers, nums, and an array of requests where
# requests[i] = [starti, endi]. The i^th request asks for the sum of
# nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both
# starti and endi are 0-indexed.
#
# Return the maximum total sum of all requests among all permutations of nums.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
# Output: 19
# Explanation: One permutation of nums is [2,1,3,4,5] with the following
# result:
# requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
# requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
# Total sum: 8 + 3 = 11.
# A permutation with a higher total sum is [3,5,4,2,1] with the following
# result:
# requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
# requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
# Total sum: 11 + 8 = 19, which is the best that you can do.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
# Output: 11
# Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with
# request sums [11].
#
# Example 3:
#
#
# Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
# Output: 47
# Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with
# request sums [19,18,10].
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^5
# 0 <= nums[i] <= 10^5
# 1 <= requests.length <= 10^5
# requests[i].length == 2
# 0 <= starti <= endi < n
#
#
#
class Solution:
    def maxSumRangeQuery(self, nums: List[int],
                         requests: List[List[int]]) -> int:
        n = len(nums)
        cc = [0] * n
        for r in requests:
            a, b = r
            cc[a] += 1
            if b + 1 < n: cc[b + 1] -= 1
        for i in range(1, n):
            cc[i] += cc[i - 1]
        nums.sort()
        cc.sort()
        return sum(map(lambda p: p[0] * p[1], zip(cc, nums))) % MOD


sol = Solution()

nums, requests = [1, 2, 3, 4, 5], [[1, 3], [0, 1]]
nums, requests = [1, 2, 3, 4, 5, 6], [[0, 1]]
nums, requests = [1, 2, 3, 4, 5, 10], [[0, 2], [1, 3], [1, 1]]
print(sol.maxSumRangeQuery(nums, requests))
