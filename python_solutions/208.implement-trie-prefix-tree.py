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
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (45.25%)
# Total Accepted:    267.9K
# Total Submissions: 586.8K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
#   '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.trie 
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.startsWith(word + '#')
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.trie 
        for c in prefix:
            if c not in root: 
                return False 
            root = root[c]
        return True
        

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
print(obj.insert("app"))
print(obj.search("app"))






