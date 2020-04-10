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
# @lc app=leetcode id=828 lang=python3
#
# [828] Count Unique Characters of All Substrings of a Given String
#
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/
#
# algorithms
# Hard (43.71%)
# Total Accepted:    8.5K
# Total Submissions: 19.5K
# Testcase Example:  '"ABC"'
#
# Let's define a function countUniqueChars(s) that returns the number of unique
# characters on s, for example if s = "LEETCODE" then "L", "T","C","O","D" are
# the unique characters since they appear only once in s, therefore
# countUniqueChars(s) = 5.
#
# On this problem given a string s we need to return the sum of
# countUniqueChars(t) where t is a substring of s. Notice that some substrings
# can be repeated so on this case you have to count the repeated ones too.
#
# Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.
#
#
# Example 1:
#
#
# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
#
#
# Example 2:
#
#
# Input: s = "ABA"
# Output: 8
# Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
#
#
# Example 3:
#
#
# Input: s = "LEETCODE"
# Output: 92
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 10^4
# s contain upper-case English letters only.
#
#
#


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pre_idx = [[-1, -1] for _ in range(26)]
        res = 0
        cnt = [0] * (1 + len(s))

        for j, e in enumerate(s):
            aux = pre_idx[ord(e) - 65]

            if aux[-1] == -1:
                cnt[j] = j + 1 + cnt[j - 1]
            else:
                cnt[j] = j - aux[1] + cnt[j - 1] - (aux[1] - aux[0])

            pre_idx[ord(e) - 65] = [aux[1], j]
            res += cnt[j]
            # print(j, res, cnt[j])
        return res % (10 ** 9 + 7)


sol = Solution()
s = "LEETCODE"
s = "BABABBABAA"
# s = "bababb"
print(sol.uniqueLetterString(s))
