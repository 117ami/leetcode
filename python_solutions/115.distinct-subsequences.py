from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
from functools import reduce 
true = True
false = False
#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (36.33%)
# Total Accepted:    119.9K
# Total Submissions: 329.5K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
# 
# Example 1:
# 
# 
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# 
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 
# 
# Example 2:
# 
# 
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# 
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
# 
# 
#
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i, substr):
            if (i, substr) in memo:
                return memo[(i, substr)]
            
            if i >= len(s) or len(s) - i < len(substr): 
                return 0 
            
            # print(i, substr)
            if len(substr) == 1:
                m = s[i:].count(substr)
                memo[(i, substr)] = m 
                return m 
            
            m = 0 
            for j in range(i, len(s)):
                if substr[0] == s[j]:
                    m += dfs(j + 1, substr[1:])
            memo[(i, substr)] = m 
            return m 
            
        return dfs(0, t)
        # return memo 

s = Solution()
s1,t = "babgbag", "bag"
# s1 = "bbag"
s1, t =  "rabbbit", "rabbit"
print(s.numDistinct(s1, t))

