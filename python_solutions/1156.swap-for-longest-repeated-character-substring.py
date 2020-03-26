from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1156 lang=python3
#
# [1156] Swap For Longest Repeated Character Substring
#
# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/description/
#
# algorithms
# Medium (47.70%)
# Total Accepted:    7.1K
# Total Submissions: 14.9K
# Testcase Example:  '"ababa"'
#
# Given a string text, we are allowed to swap two of the characters in the
# string. Find the length of the longest substring with repeated characters.
#
#
# Example 1:
#
#
# Input: text = "ababa"
# Output: 3
# Explanation: We can swap the first 'b' with the last 'a', or the last 'b'
# with the first 'a'. Then, the longest repeated character substring is "aaa",
# which its length is 3.
#
#
# Example 2:
#
#
# Input: text = "aaabaaa"
# Output: 6
# Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get
# longest repeated character substring "aaaaaa", which its length is 6.
#
#
# Example 3:
#
#
# Input: text = "aaabbaaa"
# Output: 4
#
#
# Example 4:
#
#
# Input: text = "aaaaa"
# Output: 5
# Explanation: No need to swap, longest repeated character substring is
# "aaaaa", length is 5.
#
#
# Example 5:
#
#
# Input: text = "abcdef"
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= text.length <= 20000
# text consist of lowercase English characters only.
#
#


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)
        res = prev = prevprev = cur = 0 
        prev_c = ""
        
        for i, c in enumerate(text + '/'):
            if c == prev_c:
                cur += 1
            else:
                extra = 1 if prevprev + cur < cnt[prev_c] else 0 
                res = max(res, prevprev + cur + extra)
                if i >= 2 and text[i-2] == c:
                    prevprev = prev
                else:
                    prevprev = 0 
                prev = cur 
                cur = 1 
                prev_c = c 
        return res 


sol = Solution()
text = "abcdef"
text = "ababa"
# text = "aaabaaa"
# text = "aaaaa"
# text = "bbababaaaa"
print(sol.maxRepOpt1(text))

