from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1316 lang=python3
#
# [1316] Distinct Echo Substrings
#
# https://leetcode.com/problems/distinct-echo-substrings/description/
#
# algorithms
# Hard (37.29%)
# Total Accepted:    1.4K
# Total Submissions: 3.8K
# Testcase Example:  '"abcabcabc"'
#
# Return the number of distinct non-empty substrings of text that can be
# written as the concatenation of some string with itself.
# 
# 
# Example 1:
# 
# 
# Input: text = "abcabcabc"
# Output: 3
# Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
# 
# 
# Example 2:
# 
# 
# Input: text = "leetcodeleetcode"
# Output: 2
# Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text.length <= 2000
# text has only lowercase English letters.
# 
#
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        res = set()
        ix = {}
        for i, c in enumerate(text):
            if c in ix:
                for j in ix[c][::-1]:
                    if i + i - j > len(text): break # Early stopping 
                    if text[j:i] == text[i:i+i-j]:
                        res.add(text[j:i+i-j])
                ix[c].append(i)
            else:
                ix[c] = [i]
        return len(res) 

sol = Solution()
text = "abcabcabc"
text = "leetcodeleetcode"
# text = "a" * 2000
text = "tkfbgwgqvdsbnukcpxlpifuhbvtdxhhhqurotspohiuwhblnra"
# text = "dxhhhqu"
print(sol.distinctEchoSubstrings(text))


