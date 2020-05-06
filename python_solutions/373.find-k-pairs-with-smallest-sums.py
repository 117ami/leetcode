from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
import heapq
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (35.85%)
# Total Accepted:    93.6K
# Total Submissions: 260.8K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# You are given two integer arrays nums1 and nums2 sorted in ascending order
# and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and
# one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
#
# Example 1:
#
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
# Example 2:
#
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
# Example 3:
#
#
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
#
#
#


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        res = []
        if not nums1 or not nums2 or k <= 0: return res 
        arr = [[nums1[0] + nums2[j], 0, j] for j in range(len(nums2))]
        heapq.heapify(arr)

        while k > 0 and len(arr):
            _, i, j = heapq.heappop(arr)
            res.append([nums1[i], nums2[j]])
            if i < len(nums1) - 1:
                heapq.heappush(arr, [nums1[i + 1] + nums2[j], i + 1, j])
            k -= 1
        return res


sol = Solution()
n1, n2 = [1, 1,2], [1,2,3]
# n1, n2=[],[]
print(sol.kSmallestPairs(n1, n2, 3))
