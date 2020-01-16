from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br, insort
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#
# https://leetcode.com/problems/sliding-window-median/description/
#
# algorithms
# Hard (34.90%)
# Total Accepted:    37.6K
# Total Submissions: 107.8K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# Examples:
# [2,3,4] , the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position. Your
# job is to output the median array for each window in the original array.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
#
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
# ⁠1 [3  -1  -3] 5  3  6  7       -1
# ⁠1  3 [-1  -3  5] 3  6  7       -1
# ⁠1  3  -1 [-3  5  3] 6  7       3
# ⁠1  3  -1  -3 [5  3  6] 7       5
# ⁠1  3  -1  -3  5 [3  6  7]      6
#
#
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
#
# Note:
# You may assume k is always valid, ie: k is always smaller than input array's
# size for non-empty array.
#


class Solution:
    def medianSlidingWindow(self, nums, k):
        part = sorted(nums[:k - 1])
        res = []
        for i in range(k - 1, len(nums)):
            if i >= k:
                part.pop(bl(part, nums[i - k]))
            insort(part, nums[i])
            med = part[k //
                       2] if k & 1 else (part[k // 2] + part[k // 2 - 1]) / 2.0
            res.append(med)
        return res


sol = Solution()
nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
nums, k = [1, 4, 2, 3], 4
print(sol.medianSlidingWindow(nums, k))
