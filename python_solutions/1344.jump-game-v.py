from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Jump Game V
#
# https://leetcode.com/problems/jump-game-v/description/
#
# algorithms
# Hard (52.78%)
# Total Accepted:    2.9K
# Total Submissions: 5.5K
# Testcase Example:  '[6,4,14,6,8,13,9,7,10,6,12]\n2'
#
# Given an array of integers arr and an integer d. In one step you can jump
# from index i to index:
#
#
# i + x where: i + x < arr.length and  0 < x <= d.
# i - x where: i - x >= 0 and  0 < x <= d.
#
#
# In addition, you can only jump from index i to index j if arr[i] > arr[j] and
# arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) <
# k < max(i, j)).
#
# You can choose any index of the array and start jumping. Return the maximum
# number of indices you can visit.
#
# Notice that you can not jump outside of the array at any time.
#
#
# Example 1:
#
#
# Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
# Output: 4
# Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as
# shown.
# Note that if you start at index 6 you can only jump to index 7. You cannot
# jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is
# between index 4 and 6 and 13 > 9.
# Similarly You cannot jump from index 3 to index 2 or index 1.
#
#
# Example 2:
#
#
# Input: arr = [3,3,3,3,3], d = 3
# Output: 1
# Explanation: You can start at any index. You always cannot jump to any
# index.
#
#
# Example 3:
#
#
# Input: arr = [7,6,5,4,3,2,1], d = 1
# Output: 7
# Explanation: Start at index 0. You can visit all the indicies.
#
#
# Example 4:
#
#
# Input: arr = [7,1,7,1,7,1], d = 2
# Output: 2
#
#
# Example 5:
#
#
# Input: arr = [66], d = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 10^5
# 1 <= d <= arr.length
#
#


class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [0] * n

        def helper(i):
            if dp[i]: return dp[i]
            dp[i] = 1
            for j in range(i+1, i + d + 1):
                if len(arr) <= j or arr[j] >= arr[i]: break 
                dp[i] = max(dp[i], helper(j) + 1)

            for j in range(i-1, i-d-1, -1):
                if j < 0 or arr[j] >= arr[i]:break 
                dp[i] = max(dp[i], helper(j) + 1)
            
            return dp[i]

        for i in range(n):
            helper(i)

        return max(dp)


sol = Solution()
arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
d = 2
# arr, d = [7, 6, 5, 4, 3, 2, 1], 1
arr, d = [22,29,52,97,29,75,78,2,92,70,90,12,43,17,97,18,58,100,41,32], 17
arr, d = [59,8,74,27,92,36,95,78,73,54,75,37,42,15,59,84,66,25,35,61,97,16,6,52,49,18,22,70,5,59,92,85], 20
arr, d = [6,4,14,6,8,13,9,7,10,6,12], 2
print(sol.maxJumps(arr, d))
