from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
from functools import reduce 
true = True
false = False
#
# @lc app=leetcode id=1187 lang=python3
#
# [1187] Make Array Strictly Increasing
#
# https://leetcode.com/problems/make-array-strictly-increasing/description/
#
# algorithms
# Hard (40.36%)
# Total Accepted:    3.5K
# Total Submissions: 8.7K
# Testcase Example:  '[1,5,3,6,7]\n[1,3,2,4]'
#
# Given two integer arrays arr1 and arr2, return the minimum number of
# operations (possibly zero) needed to make arr1 strictly increasing.
# 
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j
# < arr2.length and do the assignment arr1[i] = arr2[j].
# 
# If there is no way to make arr1 strictly increasing, return -1.
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# Output: 1
# Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
# 
# 
# Example 2:
# 
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# Output: 2
# Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6,
# 7].
# 
# 
# Example 3:
# 
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# Output: -1
# Explanation: You can't make arr1 strictly increasing.
# 
# 
# Constraints:
# 
# 
# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10^9
# 
# 
# 
#
INF = 0x3f3f3f3f
class Solution:
    def makeArrayIncreasing(self, a,b):
        b = sorted(list(set(b)))
        dp = {-1:0}
        for i in a:
            curr = defaultdict(lambda : INF)
            for k in dp:
                if i > k:
                    curr[i] = min(curr[i], dp[k])
                idx = bisect_right(b, k)
                if idx < len(b):
                    repl = b[idx]
                    curr[repl] = min(curr[repl], dp[k] + 1)
            dp = curr 
        return min(dp.values()) if dp else -1

s = Solution()
a,b = [5,3,7,7],[3,4,6]
# a,b = [5, 4,7],[6]
# a,b=[1,5,3,6,7], [1,3,6,6]
print(s.makeArrayIncreasing(a,b))

