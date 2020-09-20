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
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/
#
# algorithms
# Easy (77.48%)
# Total Accepted:    5.1K
# Total Submissions: 6.6K
# Testcase Example:  '[1,4,2,5,3]'
#
# Given an array of positive integers arr, calculate the sum of all possible
# odd-length subarrays.
#
# A subarray is a contiguous subsequence of the array.
#
# Return the sum of all odd-length subarrays of arr.
#
#
# Example 1:
#
#
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 =
# 58
#
# Example 2:
#
#
# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum
# is 3.
#
# Example 3:
#
#
# Input: arr = [10,11,12]
# Output: 66
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 1000
#
#
#
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        for i in range(len(arr)):
            j = i - 1
            while j >= 0:
                ans += arr[i] - arr[j]
                j -= 2
            if j == -1: ans += arr[i]
        return ans


sol = Solution()

arr = [1, 4, 2, 5, 3]
# arr = [1, 2]
# arr = [10, 11, 12]
print(sol.sumOddLengthSubarrays(arr))
