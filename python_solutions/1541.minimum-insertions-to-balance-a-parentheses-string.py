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
# @lc app=leetcode id=1541 lang=python3
#
# [1541] Minimum Insertions to Balance a Parentheses String
#
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/
#
# algorithms
# Medium (33.24%)
# Total Accepted:    3K
# Total Submissions: 8.8K
# Testcase Example:  '"(()))"'
#
# Given a parentheses string s containing only the characters '(' and ')'. A
# parentheses string is balanced if:
#
#
# Any left parenthesis '(' must have a corresponding two consecutive right
# parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right
# parenthesis '))'.
#
#
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))"
# and "(()))" are not balanced.
#
# You can insert the characters '(' and ')' at any position of the string to
# balance it if needed.
#
# Return the minimum number of insertions needed to make s balanced.
#
#
# Example 1:
#
#
# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only
# ')' matching. We need to to add one more ')' at the end of the string to be
# "(())))" which is balanced.
#
#
# Example 2:
#
#
# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.
#
#
# Example 3:
#
#
# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last
# '('.
#
#
# Example 4:
#
#
# Input: s = "(((((("
# Output: 12
# Explanation: Add 12 ')' to balance the string.
#
#
# Example 5:
#
#
# Input: s = ")))))))"
# Output: 5
# Explanation: Add 4 '(' at the beginning of the string and one ')' at the end.
# The string becomes "(((())))))))".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of '(' and ')' only.
#
#


class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace('))', ']')
        res = s.count(')')
        s = s.replace(')', ']')
        st = []

        for c in s:
            if c == '(':
                st.append(c)
            else:
                if not st:
                    res += 1
                else:
                    st.pop()
        return res + len(st) * 2


sol = Solution()


s = "(()))"
# s = "())"
# s = "))())("
# s = "(((((("
# s = ")))))))"
print(sol.minInsertions(s))
