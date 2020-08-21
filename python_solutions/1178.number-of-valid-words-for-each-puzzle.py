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
# @lc app=leetcode id=1178 lang=python3
#
# [1178] Number of Valid Words for Each Puzzle
#
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/description/
#
# algorithms
# Hard (37.87%)
# Total Accepted:    6.2K
# Total Submissions: 16.3K
# Testcase Example:  '["aaaa","asas","able","ability","actt","actor","access"]\n' +
# '["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]'
#
# With respect to a given puzzle string, a word is valid if both the following
# conditions are satisfied:
#
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced",
# "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include
# "a") and "based" (includes "s" which isn't in the puzzle).
#
# Return an array answer, where answer[i] is the number of words in the given
# word list words that are valid with respect to the puzzle puzzles[i].
#
# Example :
#
#
# Input:
# words = ["aaaa","asas","able","ability","actt","actor","access"],
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# Explanation:
# 1 valid word for "aboveyz" : "aaaa"
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There're no valid words for "gaswxyz" cause none of the words in the list
# contains letter 'g'.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 10^5
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10^4
# puzzles[i].length == 7
# words[i][j], puzzles[i][j] are English lowercase letters.
# Each puzzles[i] doesn't contain repeated characters.
#
#
#


class Solution:
    def findNumOfValidWords(
            self,
            words: List[str],
            puzzles: List[str]) -> List[int]:

        def _bin_repr(word):
            return reduce(lambda a, b: a | 1 << (ord(b) - 97), word, 0)

        cc = Counter(map(_bin_repr, words))

        res = []
        for p in puzzles:
            sub = mask = _bin_repr(p)
            first = 1 << (ord(p[0]) - ord('a'))

            c = 0
            while sub > 0:
                '''
                1. sub is one of all possible combination of p
                2. if sub contains the first char of p, and sub is contained in some word, then
                result += the frequency of sub
                '''
                if (sub & first) == first and sub in cc:
                    c += cc[sub]
                sub = (sub - 1) & mask
            res.append(c)
        return res


sol = Solution()

words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]

print(sol.findNumOfValidWords(words, puzzles))

# n = 11
# sub = n
# print(bin(n))
# while True:
# 	sub = (sub - 1) & n
# 	print(bin(sub), sub, n)
# 	if sub == 0: break
# print(ord('a'))
