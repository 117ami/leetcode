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
# @lc app=leetcode id=1577 lang=python3
#
# [1577] Number of Ways Where Square of Number Is Equal to Product of Two Numbers
#
# https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/description/
#
# algorithms
# Medium (34.04%)
# Total Accepted:    5.3K
# Total Submissions: 15.4K
# Testcase Example:  '[7,4]\n[5,2,8,9]'
#
# Given two arrays of integers nums1 and nums2, return the number of triplets
# formed (type 1 and type 2) under the following rules:
#
#
# Type 1: Triplet (i, j, k) if nums1[i]^2 == nums2[j] * nums2[k] where 0 <= i <
# nums1.length and 0 <= j < k < nums2.length.
# Type 2: Triplet (i, j, k) if nums2[i]^2 == nums1[j] * nums1[k] where 0 <= i <
# nums2.length and 0 <= j < k < nums1.length.
#
#
#
# Example 1:
#
#
# Input: nums1 = [7,4], nums2 = [5,2,8,9]
# Output: 1
# Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 *
# 8).
#
#
# Example 2:
#
#
# Input: nums1 = [1,1], nums2 = [1,1,1]
# Output: 9
# Explanation: All Triplets are valid, because 1^2 = 1 * 1.
# Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 =
# nums2[j] * nums2[k].
# Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].
#
#
# Example 3:
#
#
# Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
# Output: 2
# Explanation: There are 2 valid triplets.
# Type 1: (3,0,2).  nums1[3]^2 = nums2[0] * nums2[2].
# Type 2: (3,0,1).  nums2[3]^2 = nums1[0] * nums1[1].
#
#
# Example 4:
#
#
# Input: nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
# Output: 0
# Explanation: There are no valid triplets.
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 1000
# 1 <= nums1[i], nums2[i] <= 10^5
#
#
#
class Solution:
    def numTriplets(self, na: List[int], nb: List[int]) -> int:
        ca = Counter(map(lambda x: x * x, na))
        cb = Counter(map(lambda x: x * x, nb))
        res = 0
        for i, n in enumerate(na):
            res += sum(map(lambda j: cb[n * na[j]], range(i + 1, len(na))))
        for i, n in enumerate(nb):
            res += sum(map(lambda j: ca[n * nb[j]], range(i + 1, len(nb))))
        return res


sol = Solution()

nums1, nums2 = [7, 4], [5, 2, 8, 9]
nums1, nums2 = [1, 1], [1, 1, 1]
# nums1, nums2 = [7,7,8,3], [1,2,9,7]
# nums1, nums2 = [4,7,9,11,23], [3,5,1024,12,18]
print(sol.numTriplets(nums1, nums2))
