from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/description/
#
# algorithms
# Hard (40.64%)
# Total Accepted:    2.9K
# Total Submissions: 7.2K
# Testcase Example:  '[9,3,5]'
#
# Given an array of integers target. From a starting array, A consisting of all
# 1's, you may perform the following procedure :
# 
# 
# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < target.size and set the value of A at
# index i to x.
# You may repeat this procedure as many times as needed.
# 
# 
# Return True if it is possible to construct the target array from A otherwise
# return False.
# 
# 
# Example 1:
# 
# 
# Input: target = [9,3,5]
# Output: true
# Explanation: Start with [1, 1, 1] 
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done
# 
# 
# Example 2:
# 
# 
# Input: target = [1,1,1,2]
# Output: false
# Explanation: Impossible to create target array from [1,1,1,1].
# 
# 
# Example 3:
# 
# 
# Input: target = [8,5]
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# N == target.length
# 1 <= target.length <= 5 * 10^4
# 1 <= target[i] <= 10^9
# 
# 
#
import heapq
class Solution:
    def isPossible(self, target):
        xsum, n = sum(target), len(target)
        target = [-1 * i for i in target]
        heapq.heapify(target)
        while xsum > n:
            ax = abs(heapq.heappop(target))
            if ax <= xsum - ax:
                return false 
            heapq.heappush(target, xsum - ax * 2)
            xsum = ax
        return len(target) == n

        
sol = Solution()
target = [9,3,5]
# target = [1,1,1,2]
# target = [8, 5]
# target = [1,49,11,1,25,1,7]
print(sol.isPossible(target))




