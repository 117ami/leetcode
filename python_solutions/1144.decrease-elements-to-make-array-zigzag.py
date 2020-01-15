from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1144 lang=python3
#
# [1144] Decrease Elements To Make Array Zigzag
#
# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/description/
#
# algorithms
# Medium (44.12%)
# Total Accepted:    6.6K
# Total Submissions: 14.9K
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of integers, a move consists of choosing any element and
# decreasing it by 1.
#
# An array A is a zigzag array if either:
#
#
# Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1]
# < A[2] > A[3] < A[4] > ...
# OR, every odd-indexed element is greater than adjacent elements, ie. A[0] <
# A[1] > A[2] < A[3] > A[4] < ...
#
#
# Return the minimum number of moves to transform the given array nums into a
# zigzag array.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: 2
# Explanation: We can decrease 2 to 0 or 3 to 1.
#
#
# Example 2:
#
#
# Input: nums = [9,6,1,6,2]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
#
#
#


class Solution:
    def movesToMakeZigzag(self, nums):
        nums = [MAX] + nums + [MAX]
        res = [0, 0]
        for i in range(1, len(nums) - 1):
            res[i & 1] += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
        return min(res)


sol = Solution()
nums = [9, 6, 1, 6, 2]
nums = [2, 7, 10, 9, 8, 9]
nums = [7,5,6,100,0,100]
print(sol.movesToMakeZigzag(nums))
