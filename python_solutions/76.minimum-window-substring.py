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
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (34.68%)
# Total Accepted:    414.9K
# Total Submissions: 1.2M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
#
#
#
class Solution:
    """ Given a string S and a string T, find the minimum window in S which will
    contain all the characters in T in complexity O(n).
    """
    def minWindow(self, s: str, t: str) -> str:
        cc = Counter(t)  # Hash table to store char frequency
        unmatched_cnt = len(t)  # Total number of unmatched chars from t.
        start, end, left = 0, math.inf, 0

        for j, char in enumerate(s):
            if cc[char] > 0:
                unmatched_cnt -= 1
            cc[char] -= 1
            if unmatched_cnt == 0:  # All chars were matched
                # Remove chars not from t to find the real start. On existing
                # while loop, the code must stops on some letter c from t, as
                # for any c' in s - t, cc[c'] <= 0, and it equals 0 only
                # when s[i] in t.
                while left < j and cc[s[left]] < 0:
                    cc[s[left]] += 1
                    left += 1
                if j - left < end - start:  # Update window
                    start, end = left, j

        return s[start:end + 1] if end < math.inf else ""


sol = Solution()
S, T = "ADOBECODEBANCCC", "ABC"
# S, T = "a", "b"
# S, T = "aaaaaaaaaaaabbbbbcdd", "abcdd"
# S, T = "a", "aa"
print(sol.minWindow(S, T))
