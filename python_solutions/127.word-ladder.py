from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (26.76%)
# Total Accepted:    337.2K
# Total Submissions: 1.3M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#


class Solution:
    def ladderLength(self, b, e, wl):
        s = set(wl)
        if e not in s:
            return 0
        ladder = 2
        forward, backward = {b}, {e}

        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward

            next_forward = set()
            for w in forward:
                for i, c in enumerate(w):
                    for mid in string.ascii_lowercase:
                        nw = w[:i] + mid + w[i + 1:]
                        if nw in backward:
                            return ladder

                        if nw in s:
                            s.discard(nw)
                            next_forward.add(nw)
            forward = next_forward
            ladder += 1
        return 0


sol = Solution()
b, e, wl = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
print(sol.ladderLength(b, e, wl))
# print(chr(99))
