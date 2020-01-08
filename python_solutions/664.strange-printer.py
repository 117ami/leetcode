from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#
# https://leetcode.com/problems/strange-printer/description/
#
# algorithms
# Hard (38.56%)
# Total Accepted:    11.8K
# Total Submissions: 30.4K
# Testcase Example:  '"aaabbb"'
#
#
# There is a strange printer with the following two special requirements:
#
#
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending
# at any places, and will cover the original existing characters.
#
#
#
#
#
# Given a string consists of lower English letters only, your job is to count
# the minimum number of turns the printer needed in order to print it.
#
#
# Example 1:
#
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
#
#
#
# Example 2:
#
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of
# the string, which will cover the existing character 'a'.
#
#
#
# Hint: Length of the given string will not exceed 100.
#


class Solution:
    def strangePrinter(self, s: str) -> int:
        s = ''.join(a for a, b in zip(s, s[1:] + ' ') if a != b)
        n = len(s)
        if n < 2:
            return n
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):
            for d in range(1, n - i):
                j = i + d
                dp[i][j] = 0x3f3f3f3f
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                if s[i] == s[j]:
                    dp[i][j] -= 1
        return dp[0][-1]


sol = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaba"
# s = "aaabbb"
# s = "babababd"
# s = "dddccbdbababaddcbcaabdbdddcccddbbaabddb"
s = "dddccbdbababaddcbcaabdbdddcccddbbaabddb"
# s = "aaaaaaa"
# text = ''.join(a for a, b in zip(s, s[1:] + ' ') if a != b)
# print(text)
# s = "byrvzpjpnbwcgdiqmoydqkojfveyjehmueqbagdaspnqvwsvaucenswlvzpgpnjlwjuzhbncpwcyurynwbzwpvhnmmuujwubulro"
# print(set(s))
# print(s.split('a'))
print(sol.strangePrinter(s))
