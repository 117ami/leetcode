from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
true = True
false = False
#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
#
# algorithms
# Hard (44.74%)
# Total Accepted:    31.3K
# Total Submissions: 70K
# Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
#
# In a given array nums of positive integers, find three non-overlapping
# subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k
# entries.
#
# Return the result as a list of indices representing the starting position of
# each interval (0-indexed). If there are multiple answers, return the
# lexicographically smallest one.
#
# Example:
#
#
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting
# indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be
# lexicographically larger.
#
#
#
#
# Note:
#
#
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).
#
#
#
#
#


class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        best1 = 0
        best2 = [0, k]
        best3 = [0, k, 2 * k]

        sum1 = sum(nums[: k])
        sum2 = sum(nums[k: 2 * k])
        sum3 = sum(nums[2 * k: 3 * k])

        best_sum1 = sum1
        best_sum2 = sum1 + sum2
        best_sum3 = sum1 + sum2 + sum3

        p1, p2, p3 = 1, k + 1, 2 * k + 1
        while p3 <= len(nums) - k:
            sum1 = sum1 + nums[p1 + k - 1] - nums[p1 - 1]
            sum2 = sum2 + nums[p2 + k - 1] - nums[p2 - 1]
            sum3 = sum3 + nums[p3 + k - 1] - nums[p3 - 1]

            if sum1 > best_sum1:
                best1 = p1
                best_sum1 = sum1

            if best_sum1 + sum2 > best_sum2:
                best2 = [best1, p2]
                best_sum2 = best_sum1 + sum2

            if best_sum2 + sum3 > best_sum3:
                best3 = best2 + [p3]
                best_sum3 = best_sum2 + sum3

            p1 += 1
            p2 += 1
            p3 += 1

        return best3


s = Solution()
ns, k = [1, 2, 1, 2, 6, 7, 5, 1], 2
ns, k = [7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3
print(s.maxSumOfThreeSubarrays(ns, k))
