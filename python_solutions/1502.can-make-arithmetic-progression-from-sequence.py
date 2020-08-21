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
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
#
# algorithms
# Easy (81.44%)
# Total Accepted:    6.6K
# Total Submissions: 8.1K
# Testcase Example:  '[3,5,1]'
#
# Given an array of numbers arr. A sequence of numbers is called an arithmetic
# progression if the difference between any two consecutive elements is the
# same.
#
# Return true if the array can be rearranged to form an arithmetic progression,
# otherwise, return false.
#
#
# Example 1:
#
#
# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with
# differences 2 and -2 respectively, between each consecutive elements.
#
#
# Example 2:
#
#
# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic
# progression.
#
#
#
# Constraints:
#
#
# 2 <= arr.length <= 1000
# -10^6 <= arr[i] <= 10^6
#
#


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return len(
            set(map(lambda i: arr[i] - arr[i - 1], range(1, len(arr))))) == 1


sol = Solution()
arr = [3, 5, 1]
# arr = [1, 2, 4]
print(sol.canMakeArithmeticProgression(arr))
