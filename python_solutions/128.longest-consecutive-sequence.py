from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (43.40%)
# Total Accepted:    250.6K
# Total Submissions: 577.1K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
#


class Solution:
    def longestConsecutive(self, nums):
        ss = set(nums)
        best = 0
        for n in ss:
            if n - 1 not in ss:
                p = n + 1
                while p in ss:
                    p += 1
                best = max(best, p - n)
        return best 


sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))