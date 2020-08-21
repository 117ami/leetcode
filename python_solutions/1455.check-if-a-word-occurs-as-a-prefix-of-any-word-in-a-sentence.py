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
# @lc app=leetcode id=1455 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/
#
# algorithms
# Easy (67.29%)
# Total Accepted:    8.3K
# Total Submissions: 12.4K
# Testcase Example:  '"i love eating burger"\n"burg"'
#
# Given a sentence that consists of some words separated by a single space, and
# a searchWord.
# 
# You have to check if searchWord is a prefix of any word in sentence.
# 
# Return the index of the word in sentence where searchWord is a prefix of this
# word (1-indexed).
# 
# If searchWord is a prefix of more than one word, return the index of the
# first word (minimum index). If there is no such word return -1.
# 
# A prefix of a string S is any leading contiguous substring of S.
# 
# 
# Example 1:
# 
# 
# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the
# sentence.
# 
# 
# Example 2:
# 
# 
# Input: sentence = "this problem is an easy problem", searchWord = "pro"
# Output: 2
# Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word
# in the sentence, but we return 2 as it's the minimal index.
# 
# 
# Example 3:
# 
# 
# Input: sentence = "i am tired", searchWord = "you"
# Output: -1
# Explanation: "you" is not a prefix of any word in the sentence.
# 
# 
# Example 4:
# 
# 
# Input: sentence = "i use triple pillow", searchWord = "pill"
# Output: 4
# 
# 
# Example 5:
# 
# 
# Input: sentence = "hello from the other side", searchWord = "they"
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= sentence.length <= 100
# 1 <= searchWord.length <= 10
# sentence consists of lowercase English letters and spaces.
# searchWord consists of lowercase English letters.
# 
#
class Solution:
    def isPrefixOfWord(self, s: str, w: str) -> int:
        for i, c in enumerate(s.split(' '), 1):
            if c.startswith(w):
                return i 
        return -1
        

sol = Solution()
s = 'i use triple pillow'
w = 'pil'
print(sol.isPrefixOfWord(s, w))

