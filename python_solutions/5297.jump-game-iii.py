from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
from functools import reduce 
import string
true = True
false = False
#
# @lc app=leetcode id=5297 lang=python3
#
# [5297] Jump Game III
#
# https://leetcode.com/problems/jump-game-iii/description/
#
# algorithms
# Medium (58.18%)
# Total Accepted:    2.9K
# Total Submissions: 5K
# Testcase Example:  '[4,2,3,0,3,1,2]\n5'
#
# Given an array of non-negative integers arr, you are initially positioned at
# start index of the array. When you are at index i, you can jump to i + arr[i]
# or i - arr[i], check if you can reach to any index with value 0.
# 
# Notice that you can not jump outside of the array at any time.
# 
# 
# Example 1:
# 
# 
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 
# 
# 
# Example 2:
# 
# 
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3
# 
# 
# Example 3:
# 
# 
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 5 * 10^4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length
# 
#
class Solution:
    def canReach(self, arr, sid):
        if arr[sid] == 0:
            return true
        jobs = [sid]
        seen = set()
        while jobs:
            n = jobs.pop(0)
            if n < 0 or n >= len(arr) or n in seen: 
                continue 
            seen.add(n)
            
            if arr[n] == 0:
                return true
            
            jobs += [n - arr[n], n + arr[n]]
        return false

sol = Solution()


