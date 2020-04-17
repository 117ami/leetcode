from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (34.08%)
# Total Accepted:    73.8K
# Total Submissions: 235.7K
# Testcase Example:  '"()"'
#
# 
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
# 
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
# 
# 
# 
# Example 1:
# 
# Input: "()"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "(*)"
# Output: True
# 
# 
# 
# Example 3:
# 
# Input: "(*))"
# Output: True
# 
# 
# 
# Note:
# 
# The string size will be in the range [1, 100].
# 
# 
#
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = right = 0 
        for c in s:
            left += 1 if c == '(' else -1 
            right += -1 if c == ')' else 1 
            if right < 0: return False # i.e., ')' is more that '(' + '*'
            left = max(left, 0) # i.e., all '(' are completed by either '*' or ')'
        
        return left == 0


sol = Solution()
s = "()"
s = '(*))'
s = '(())  ((())()()(*)   (*()(())())()) ()() ((()())((()))(*'
# s = '*())'
s = "((*)(*))((*"
print(sol.checkValidString(s))


