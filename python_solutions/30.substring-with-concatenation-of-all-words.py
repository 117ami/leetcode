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
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (25.41%)
# Total Accepted:    180.6K
# Total Submissions: 710.9K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
#
#
#
# Example 1:
#
#
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
#
#
#
class Solution:
    def hashit(self, s: str, words: List[str]) -> List[int]:
        list_len, word_len, res = len(words), len(words[0]) if words else 0, []
        s_len = len(s)
        ghash = sum(map(hash, words))
        for i in range(word_len):
            thash, cnt, j = 0, 0, i
            while j + word_len <= s_len:
                thash += hash(s[j:j + word_len])
                print(s[j:j + word_len])
                cnt += 1
                if cnt < list_len:
                    j += word_len
                    continue
                if cnt > list_len:
                    left_idx = j - list_len * word_len
                    thash -= hash(s[left_idx:left_idx + word_len])
                if thash == ghash:
                    res.append(j - list_len * word_len + word_len)
                j += word_len
                print(thash)

        return res

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return self.hashit(s, words)
        n, m, index = len(words), len(words[0]) if words else 0, []
        cc = Counter(words)

        for i in range(m):
            local_cc, window = defaultdict(int), deque()

            # Assume j is the starting index of some valid substring
            for j in range(i, len(s), m):
                word = s[j:j + m]
                if word in cc:
                    local_cc[word] += 1
                    window.append(word)

                    while local_cc[word] > cc[word]:
                        local_cc[window.popleft()] -= 1

                    if len(window) == n:
                        index.append(j - (n - 1) * m)
                else:
                    local_cc.clear()
                    window.clear()
        return index


sol = Solution()

s = "wordgoodgoodgoodbestword",
words = ["word", "good", "best", "word"]
# s, words = "barfoothefoobarman", ["foo", "bar"]
s, words = "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
print(sol.findSubstring(s, words))
print(hash("Good"))
print(hash("best"))
print(hash("Good"))
