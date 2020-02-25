from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
#
# algorithms
# Medium (44.60%)
# Total Accepted:    3.1K
# Total Submissions: 6.2K
# Testcase Example:  '"abcabc"'
#
# Given a string s consisting only of characters a, b and c.
# 
# Return the number of substrings containing at least one occurrence of all
# these characters a, b and c.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab",
# "bcabc", "cab", "cabc" and "abc" (again). 
# 
# 
# Example 2:
# 
# 
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "aaacb", "aacb" and "acb". 
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.
# 
#
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0 
        a = b = c = 0
        for i, char in enumerate(s):
            if char == 'a':
                res += min(b, c)
                a = i + 1
            elif char == 'b':
                res += min(a, c)
                b = i + 1
            else:
                res += min(a, b)
                c = i + 1
        return res 
            
sol = Solution()
ss = 'abcabc'
ss = 'aaabc'
ss = 'acbbcac'
print(sol.numberOfSubstrings(ss))



