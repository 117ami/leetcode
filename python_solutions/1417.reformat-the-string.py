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
# @lc app=leetcode id=1417 lang=python3
#
# [1417] Reformat The String
#
# https://leetcode.com/problems/reformat-the-string/description/
#
# algorithms
# Easy (54.54%)
# Total Accepted:    6.9K
# Total Submissions: 12.6K
# Testcase Example:  '"a0b1c2"'
#
# Given alphanumeric string s. (Alphanumeric string is a string consisting of
# lowercase English letters and digits).
#
# You have to find a permutation of the string where no letter is followed by
# another letter and no digit is followed by another digit. That is, no two
# adjacent characters have the same type.
#
# Return the reformatted string or return an empty string if it is impossible
# to reformat the string.
#
#
# Example 1:
#
#
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c".
# "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
#
#
# Example 2:
#
#
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by
# digits.
#
#
# Example 3:
#
#
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by
# characters.
#
#
# Example 4:
#
#
# Input: s = "covid2019"
# Output: "c2o0v1i9d"
#
#
# Example 5:
#
#
# Input: s = "ab123"
# Output: "1a2b3"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.
#
#
#


class Solution:
    def reformat(self, s: str) -> str:
        chars = [c for c in s if not c.isdigit()]
        nums = [c for c in s if c.isdigit()]
        if abs(len(chars) - len(nums)) > 1:
            return ""
        # chars.append('')
        # nums.append('')
        res = zip(chars, nums + ['']) if len(chars) > len(nums) else zip(nums, chars + [""])
        return ''.join(str(e[0]) + str(e[1]) for e in res)


sol = Solution()
print(sol.reformat("a0b1c2"))
