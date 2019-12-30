from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (41.98%)
# Total Accepted:    12K
# Total Submissions: 28.5K
# Testcase Example:  '["a==b","b!=a"]'
#
# Given an array equations of strings that represent relationships between
# variables, each string equations[i] has length 4 and takes one of two
# different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not
# necessarily different) that represent one-letter variable names.
#
# Return true if and only if it is possible to assign integers to variable
# names so as to satisfy all the given equations.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.  There is no way to assign the variables to
# satisfy both equations.
#
#
#
# Example 2:
#
#
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
#
#
#
# Example 3:
#
#
# Input: ["a==b","b==c","a==c"]
# Output: true
#
#
#
# Example 4:
#
#
# Input: ["a==b","b!=c","c==a"]
# Output: false
#
#
#
# Example 5:
#
#
# Input: ["c==c","b==d","x!=z"]
# Output: true
#
#
#
#
# Note:
#
#
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='
#
#
#
#
#
#
#
#


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    def equationsPossible(self, eqs):
        eqs.sort(key=lambda expr: '!' in expr)
        uf = UF(26)

        for e in eqs:
            if e[1] == '=':
                uf.union(ord(e[0]) - 97, ord(e[3]) - 97)
            else:
                if uf.find(ord(e[0]) - 97) == uf.find(ord(e[3]) - 97):
                    return false
        return true


sol = Solution()
eqs = ["z!=b", "a==b", "b!=c", "c==a"]
eqs = ["a!=a"]
print(sol.equationsPossible(eqs))
