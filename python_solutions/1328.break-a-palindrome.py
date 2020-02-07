from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#
# https://leetcode.com/problems/break-a-palindrome/description/
#
# algorithms
# Medium (39.93%)
# Total Accepted:    3.9K
# Total Submissions: 9.7K
# Testcase Example:  '"abccba"'
#
# Given a palindromic string palindrome, replace exactly one character by any
# lowercase English letter so that the string becomes the lexicographically
# smallest possible string that isn't a palindrome.
#
# After doing so, return the final string.  If there is no way to do so, return
# the empty string.
#
#
# Example 1:
#
#
# Input: palindrome = "abccba"
# Output: "aaccba"
#
#
# Example 2:
#
#
# Input: palindrome = "a"
# Output: ""
#
#
#
# Constraints:
#
#
# 1 <= palindrome.length <= 1000
# palindrome consists of only lowercase English letters.
#
#


class Solution:
    def breakPalindrome(self, p):
        if len(p) == 1:
            return ""
        res = 0
        for i in range(len(p) // 2):
            c = p[i]
            if c != 'a':
                return p[:i] + 'a' + p[i + 1:]
        return p[:-1] + 'b'


sol = Solution()
p = "abccba"
p = "aba"
print(sol.breakPalindrome(p))
