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
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
#
# algorithms
# Medium (48.61%)
# Total Accepted:    8.2K
# Total Submissions: 16.8K
# Testcase Example:  '"abciiidef"\n3'
#
# Given a string s and an integer k.
#
# Return the maximum number of vowel letters in any substring of s with length
# k.
#
# Vowel letters in English are (a, e, i, o, u).
#
#
# Example 1:
#
#
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
#
#
# Example 2:
#
#
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
#
#
# Example 3:
#
#
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
#
#
# Example 4:
#
#
# Input: s = "rhythms", k = 4
# Output: 0
# Explanation: We can see that s doesn't have any vowel letters.
#
#
# Example 5:
#
#
# Input: s = "tryhard", k = 4
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 1 <= k <= s.length
#
#


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = res = 0
        vowels = set("aeiou")
        for i, c in enumerate(s):
            if i < k:
                cnt += int(c in vowels)
            else:
                cnt += int(c in vowels) - int(s[i - k] in vowels)
            res = max(res, cnt)
        return res


sol = Solution()
s, k = "rhythms", 4
print(sol.maxVowels(s, k))
x = 1
x += 'a' == 'a'
print(x)