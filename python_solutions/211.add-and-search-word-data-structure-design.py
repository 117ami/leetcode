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
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (36.97%)
# Total Accepted:    196.1K
# Total Submissions: 528K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
#   '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
    
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    def search(self, word):
        return self.dfs(self.root, word)
    
    def dfs(self, node, word):
        if not word:
            return node.is_word

        if word[0] == ".":
            for n in node.children.values():
                if self.dfs(n, word[1:]):
                    return True 
        else:
            node = node.children.get(word[0])
            if node:
                return self.dfs(node, word[1:])
        return False 

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("pad")
print(obj.search('..d'))

