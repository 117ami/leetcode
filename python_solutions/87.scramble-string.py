from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#
# https://leetcode.com/problems/scramble-string/description/
#
# algorithms
# Hard (32.61%)
# Total Accepted:    100.3K
# Total Submissions: 307K
# Testcase Example:  '"great"\n"rgeat"'
#
# Given a string s1, we may represent it as a binary tree by partitioning it to
# two non-empty substrings recursively.
#
# Below is one possible representation of s1 = "great":
#
#
# ⁠   great
# ⁠  /    \
# ⁠ gr    eat
# ⁠/ \    /  \
# g   r  e   at
# ⁠          / \
# ⁠         a   t
#
#
# To scramble the string, we may choose any non-leaf node and swap its two
# children.
#
# For example, if we choose the node "gr" and swap its two children, it
# produces a scrambled string "rgeat".
#
#
# ⁠   rgeat
# ⁠  /    \
# ⁠ rg    eat
# ⁠/ \    /  \
# r   g  e   at
# ⁠          / \
# ⁠         a   t
#
#
# We say that "rgeat" is a scrambled string of "great".
#
# Similarly, if we continue to swap the children of nodes "eat" and "at", it
# produces a scrambled string "rgtae".
#
#
# ⁠   rgtae
# ⁠  /    \
# ⁠ rg    tae
# ⁠/ \    /  \
# r   g  ta  e
# ⁠      / \
# ⁠     t   a
#
#
# We say that "rgtae" is a scrambled string of "great".
#
# Given two strings s1 and s2 of the same length, determine if s2 is a
# scrambled string of s1.
#
# Example 1:
#
#
# Input: s1 = "great", s2 = "rgeat"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
#
#


class Solution:
    @lru_cache()
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return true 
        c1 = Counter(s1)
        c2 = Counter(s2)
        if c1 != c2:
            return false
        
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return true 
            if self.isScramble(s1[:i], s2[len(s1) - i:]) and self.isScramble(s1[i:], s2[:len(s1)-i]):
                return true 
        return false 




sol = Solution()
print(sol.isScramble('rgtae', 'great'))
print(sol.isScramble('abc', 'bca'))
