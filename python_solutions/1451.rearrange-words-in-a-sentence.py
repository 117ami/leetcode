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
# @lc app=leetcode id=1451 lang=python3
#
# [1451] Rearrange Words in a Sentence
#
# https://leetcode.com/problems/rearrange-words-in-a-sentence/description/
#
# algorithms
# Medium (48.91%)
# Total Accepted:    8.3K
# Total Submissions: 16.6K
# Testcase Example:  '"Leetcode is cool"'
#
# Given a sentence text (A sentence is a string of space-separated words) in
# the following format:
# 
# 
# First letter is in upper case.
# Each word in text are separated by a single space.
# 
# 
# Your task is to rearrange the words in text such that all words are
# rearranged in an increasing order of their lengths. If two words have the
# same length, arrange them in their original order.
# 
# Return the new text following the format shown above.
# 
# 
# Example 1:
# 
# 
# Input: text = "Leetcode is cool"
# Output: "Is cool leetcode"
# Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and
# "cool" of length 4.
# Output is ordered by length and the new first word starts with capital
# letter.
# 
# 
# Example 2:
# 
# 
# Input: text = "Keep calm and code on"
# Output: "On and keep calm code"
# Explanation: Output is ordered as follows:
# "On" 2 letters.
# "and" 3 letters.
# "keep" 4 letters in case of tie order by position in original text.
# "calm" 4 letters.
# "code" 4 letters.
# 
# 
# Example 3:
# 
# 
# Input: text = "To be or not to be"
# Output: "To be or to be not"
# 
# 
# 
# Constraints:
# 
# 
# text begins with a capital letter and then contains lowercase letters and
# single space between words.
# 1 <= text.length <= 10^5
# 
# 
#
class Solution:
    def arrangeWords(self, text: str) -> str:
        words = sorted(text.lower().split(' '), key=len)
        return ' '.join(words).capitalize()
        # text = sorted([(i, word.lower()) for i, word in enumerate(text.split(' '))], key=lambda e: (len(e[1]), e[0]))
        return ' '.join([w for _, w in text]).capitalize()

        

sol = Solution()
s="Keep calm and code on"
s="To be or not to be"
print(sol.arrangeWords(s))

