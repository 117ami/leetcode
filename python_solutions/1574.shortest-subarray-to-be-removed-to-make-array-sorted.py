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
# @lc app=leetcode id=1574 lang=python3
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/
#
# algorithms
# Medium (24.19%)
# Total Accepted:    2.2K
# Total Submissions: 9.2K
# Testcase Example:  '[1,2,3,10,4,2,3,5]'
#
# Given an integer array arr, remove a subarray (can be empty) from arr such
# that the remaining elements in arr are non-decreasing.
#
# A subarray is a contiguous subsequence of the array.
#
# Return the length of the shortest subarray to remove.
#
#
# Example 1:
#
#
# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The
# remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].
#
# Example 2:
#
#
# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a
# single element. Therefore we need to remove a subarray of length 4, either
# [5,4,3,2] or [4,3,2,1].
#
#
# Example 3:
#
#
# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove
# any elements.
#
#
# Example 4:
#
#
# Input: arr = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^9
#
#
#
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n, j = len(arr), len(arr) - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if j == 0: return 0
        ans = j
        for i in range(n):
            if i > 0 and arr[i - 1] > arr[i]: break
            while j < n and arr[i] > arr[j]:
                j += 1
            ans = min(ans, j - i - 1)
        return ans


sol = Solution()

arr = [1, 2, 3, 10, 4, 2, 3, 5]
print(sol.findLengthOfShortestSubarray(arr))
