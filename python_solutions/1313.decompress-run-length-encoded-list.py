from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#
# https://leetcode.com/problems/decompress-run-length-encoded-list/description/
#
# algorithms
# Easy (81.74%)
# Total Accepted:    2.6K
# Total Submissions: 3.2K
# Testcase Example:  '[1,2,3,4]'
#
# We are given a list nums of integers representing a list compressed with
# run-length encoding.
#
# Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]]
# (with i >= 0).  For each such pair, there are a elements with value b in the
# decompressed list.
#
# Return the decompressed list.
#
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 100
# nums.length % 2 == 0
# 1 <= nums[i] <= 100
#
#


class Solution:
    def decompressRLElist(self, nums):
        return [j for i in ([nums[i]] * nums[i - 1]
                            for i in range(1, len(nums), 2)) for j in i]


sol = Solution()
print(sol.decompressRLElist([1, 2, 3, 4]))
