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
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
#
# algorithms
# Hard (58.41%)
# Total Accepted:    13.5K
# Total Submissions: 23.1K
# Testcase Example:  '"zzazz"'
#
# Given a string s. In one step you can insert any character at any index of
# the string.
#
# Return the minimum number of steps to make s palindrome.
#
# A Palindrome String is one that reads the same backward as well as
# forward.
#
#
# Example 1:
#
#
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we don't need any
# insertions.
#
#
# Example 2:
#
#
# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
#
#
# Example 3:
#
#
# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
#
#
# Example 4:
#
#
# Input: s = "g"
# Output: 0
#
#
# Example 5:
#
#
# Input: s = "no"
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 500
# All characters of s are lower case English letters.
#
#
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def dfs(i, j):
            if i >= j: return 0
            if dp[i][j] >= 0: return dp[i][j]
            ans = dfs(
                i + 1, j -
                1) if s[i] == s[j] else 1 + min(dfs(i + 1, j), dfs(i, j - 1))
            dp[i][j] = ans
            return ans

        return dfs(0, n - 1)


sol = Solution()

s = "zzazz"
s = "mbadm"
s = "leetcode"
print(sol.minInsertions(s))
